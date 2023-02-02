import unittest

from src.log.meta_field import MetaField, MetaFieldWrongDatatype, Optionality, MetaFieldMissingMandatoryValue, \
    MetaFieldDuplicate, MetaFieldNumberOutOfRange


class TestFileParsingWithJsonOutput(unittest.TestCase):
    def test_simple_integer_field_output(self):
        test_integer_field = MetaField("field_1", int, Optionality.OPTIONAL)
        test_integer_field.set(10)
        json_result = MetaField.create_json([test_integer_field])

        self.assertEqual(10, test_integer_field.get())
        self.assertEqual({"field_1": 10}, json_result)

    def test_simple_integer_field_input(self):
        test_integer_field = MetaField("field_1", int, Optionality.OPTIONAL)
        MetaField.parse_json([test_integer_field], {"something else": 0, "field_1": 22})

        self.assertEqual(22, test_integer_field.get())

    def test_multiple_field_types_output(self):
        test_integer_field = MetaField("my_int", int, Optionality.OPTIONAL)
        test_float_field = MetaField("my_float", float, Optionality.OPTIONAL)
        test_string_field = MetaField("my_string", str, Optionality.OPTIONAL)

        test_integer_field.set(99)
        test_float_field.set(123.45)
        test_string_field.set("Hello World")

        json_result = MetaField.create_json([test_integer_field, test_float_field, test_string_field])

        self.assertEqual(99, test_integer_field.get())
        self.assertEqual(123.45, test_float_field.get())
        self.assertEqual("Hello World", test_string_field.get())
        self.assertEqual({"my_int": 99, "my_float": 123.45, "my_string": "Hello World"}, json_result)

    def test_multiple_similar_fields(self):
        input_fields = []
        output_fields = []
        for x in range(0, 6):
            output_field = MetaField("field" + str(x), int, Optionality.OPTIONAL)
            output_field.set(x * 2)
            output_fields.append(output_field)
            input_field = MetaField("field" + str(x), int, Optionality.OPTIONAL)
            input_fields.append(input_field)

        json_result = MetaField.create_json(output_fields)

        MetaField.parse_json(input_fields, json_result)

        self.assertEqual({"field0": 0, "field1": 2, "field2": 4, "field3": 6, "field4": 8, "field5": 10}, json_result)
        expected_value = 0
        for f in input_fields:
            self.assertEqual(expected_value, f.get())
            expected_value += 2

    def test_integer_cannot_contain_anything_else(self):
        test_integer_field = MetaField("my_int", int, Optionality.OPTIONAL)
        self.assertRaises(MetaFieldWrongDatatype, test_integer_field.set, "STRING VALUE")
        self.assertRaises(MetaFieldWrongDatatype, test_integer_field.set, 123.99)

        self.assertRaises(MetaFieldWrongDatatype, MetaField.parse_json, [test_integer_field], {"my_int": "STRING"})
        self.assertRaises(MetaFieldWrongDatatype, MetaField.parse_json, [test_integer_field], {"my_int": 1.2})

    def test_string_cannot_contain_anything_else(self):
        test_string_field = MetaField("my_string", str, Optionality.OPTIONAL)
        self.assertRaises(MetaFieldWrongDatatype, test_string_field.set, 40)
        self.assertRaises(MetaFieldWrongDatatype, test_string_field.set, 123.99)

        self.assertRaises(MetaFieldWrongDatatype, MetaField.parse_json, [test_string_field], {"my_string": 40})
        self.assertRaises(MetaFieldWrongDatatype, MetaField.parse_json, [test_string_field], {"my_string": 9.9})

    def test_float_cannot_contain_anything_else(self):
        test_float_field = MetaField("my_float", float, Optionality.OPTIONAL)
        self.assertRaises(MetaFieldWrongDatatype, test_float_field.set, "STRING VALUE")
        self.assertRaises(MetaFieldWrongDatatype, test_float_field.set, 456)

        self.assertRaises(MetaFieldWrongDatatype, MetaField.parse_json, [test_float_field], {"my_float": "STRING"})
        self.assertRaises(MetaFieldWrongDatatype, MetaField.parse_json, [test_float_field], {"my_float": 22222})

    def test_optionality_for_output(self):
        mandatory_field_with_value = MetaField("A", int, Optionality.MANDATORY)
        mandatory_field_without_value = MetaField("B", int, Optionality.MANDATORY)
        optional_field_with_value = MetaField("C", int, Optionality.OPTIONAL)
        optional_field_without_value = MetaField("D", int, Optionality.OPTIONAL)

        mandatory_field_with_value.set(10)
        optional_field_with_value.set(20)

        json_result = MetaField.create_json(
            [mandatory_field_with_value, optional_field_without_value, optional_field_with_value])

        self.assertEqual({"A": 10, "C": 20}, json_result)
        self.assertRaises(MetaFieldMissingMandatoryValue, MetaField.create_json, [mandatory_field_without_value])

    def test_optionality_for_input(self):
        mandatory_field_with_value = MetaField("A", int, Optionality.MANDATORY)
        mandatory_field_without_value = MetaField("B", int, Optionality.MANDATORY)
        optional_field_with_value = MetaField("C", int, Optionality.OPTIONAL)
        optional_field_without_value = MetaField("D", int, Optionality.OPTIONAL)

        input_json = {"A": 22, "C": 33}
        MetaField.parse_json([mandatory_field_with_value, optional_field_without_value, optional_field_with_value],
                             input_json)

        self.assertEqual(22, mandatory_field_with_value.get())
        self.assertEqual(33, optional_field_with_value.get())
        self.assertIsNone(optional_field_without_value.get())
        self.assertRaises(MetaFieldMissingMandatoryValue, MetaField.parse_json, [mandatory_field_without_value],
                          input_json)

    def test_duplicates_not_allowed_in_output(self):
        field_1 = MetaField("one", int, Optionality.MANDATORY)
        field_2 = MetaField("two", float, Optionality.MANDATORY)
        field_1_with_same_datatype = MetaField("one", int, Optionality.MANDATORY)
        field_2_with_different_datatype = MetaField("two", str, Optionality.MANDATORY)

        field_1.set(1)
        field_2.set(2.0)
        field_1_with_same_datatype.set(1)
        field_2_with_different_datatype.set("two")

        ok_json_1 = MetaField.create_json([field_1, field_2])
        ok_json_2 = MetaField.create_json([field_1_with_same_datatype, field_2_with_different_datatype])

        self.assertEqual({"one": 1, "two": 2.0}, ok_json_1)
        self.assertEqual({"one": 1, "two": "two"}, ok_json_2)
        self.assertRaises(MetaFieldDuplicate, MetaField.create_json, [field_1, field_1_with_same_datatype])
        self.assertRaises(MetaFieldDuplicate, MetaField.create_json, [field_2, field_2_with_different_datatype])

    def test_range_checking_set_method(self):
        upper_bound_field = MetaField("Upper", int, Optionality.MANDATORY, None, 10)
        lower_bound_field = MetaField("Upper", int, Optionality.MANDATORY, 5, None)
        range_bound_field = MetaField("Upper", int, Optionality.MANDATORY, 2, 6)

        lower_bound_field.set(6)
        lower_bound_field.set(5)
        self.assertRaises(MetaFieldNumberOutOfRange, lower_bound_field.set, 4)

        upper_bound_field.set(9)
        upper_bound_field.set(10)
        self.assertRaises(MetaFieldNumberOutOfRange, upper_bound_field.set, 11)

        range_bound_field.set(2)
        range_bound_field.set(6)
        self.assertRaises(MetaFieldNumberOutOfRange, range_bound_field.set, 1)
        self.assertRaises(MetaFieldNumberOutOfRange, range_bound_field.set, 7)

    def test_range_checking_always_works_from_json(self):
        input_json = {"int": 10, "float": 12.345}

        int_in_range = MetaField("int", int, Optionality.MANDATORY, 4, 12)
        float_in_range = MetaField("float", float, Optionality.MANDATORY, 12.344, 12.346)

        int_not_in_range = MetaField("int", int, Optionality.MANDATORY, 4, 9)
        float_not_in_range = MetaField("float", float, Optionality.MANDATORY, 912.344, 912.346)

        MetaField.parse_json([int_in_range, float_in_range], input_json)
        self.assertRaises(MetaFieldNumberOutOfRange, MetaField.parse_json, [int_not_in_range], input_json)
        self.assertRaises(MetaFieldNumberOutOfRange, MetaField.parse_json, [float_not_in_range], input_json)
