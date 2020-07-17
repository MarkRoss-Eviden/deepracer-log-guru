class EpisodeFilter:

    def __init__(self):
        self.filter_from_start_line = False
        self.filter_max_steps = None
        self.filter_min_percent = None
        self.filter_complete_section = None
        self.filter_min_average_reward = None
        self.filter_peak_track_speed = None
        self.filter_specific_waypoint_id = None
        self.filter_specific_waypoint_min_reward = None

        self.all_episodes = None

    def reset(self):
        self.filter_from_start_line = False
        self.filter_max_steps = None
        self.filter_min_percent = None
        self.filter_complete_section = None
        self.filter_min_average_reward = None
        self.filter_peak_track_speed = None
        self.filter_specific_waypoint_id = None
        self.filter_specific_waypoint_min_reward = None

    def set_filter_from_start_line(self, setting :bool):
        self.filter_from_start_line = setting

    def set_filter_max_steps(self, setting: int):
        self.filter_max_steps = setting

    def set_filter_min_percent(self, percent: int):
        self.filter_min_percent = percent

    def set_filter_min_average_reward(self, min_reward: int):
        self.filter_min_average_reward = min_reward

    def set_filter_complete_section(self, start_waypoint_id, finish_waypoint_id):
        if start_waypoint_id is not None and finish_waypoint_id is not None:
            self.filter_complete_section = (start_waypoint_id, finish_waypoint_id)
        elif start_waypoint_id is not None:
            self.filter_complete_section = (start_waypoint_id, start_waypoint_id)
        elif finish_waypoint_id is not None:
            self.filter_complete_section = (finish_waypoint_id, finish_waypoint_id)
        else:
            self.filter_complete_section = None

    def set_filter_peak_track_speed(self, peak_track_speed):
        self.filter_peak_track_speed = peak_track_speed

    def set_filter_specific_waypoint_reward(self, waypoint_id :int, min_reward :float):
        self.filter_specific_waypoint_id = waypoint_id

        if waypoint_id is not None:
            self.filter_specific_waypoint_min_reward = min_reward
        else:
            self.filter_specific_waypoint_min_reward = None

    def set_all_episodes(self, all_episodes):
        self.all_episodes = all_episodes

    def get_filtered_episodes(self):
        if not self.all_episodes:
            return None

        result = []
        for e in self.all_episodes:
            if e.is_real_start or not self.filter_from_start_line:
                if self.filter_max_steps is None or e.step_count <= self.filter_max_steps:
                    if self.filter_min_percent is None or e.percent_complete >= self.filter_min_percent:
                        if self.filter_min_average_reward is None or e.average_reward >= self.filter_min_average_reward:
                            if self.filter_peak_track_speed is None or e.peak_track_speed >= self.filter_peak_track_speed:
                                if self.matches_complete_section_filter(e):
                                    if self.matches_specific_waypoint_reward_filter(e):
                                        result.append(e)

        return result

    def matches_specific_waypoint_reward_filter(self, episode):
        if self.filter_specific_waypoint_id is None:
            return True
        else:
            for e in episode.events:
                if e.closest_waypoint_index == self.filter_specific_waypoint_id and (
                            self.filter_specific_waypoint_min_reward is None or e.reward >= self.filter_specific_waypoint_min_reward):
                    return True

        return False

    def matches_complete_section_filter(self, episode):
        if not self.filter_complete_section:
            return True

        (start, finish) = self.filter_complete_section

        actual_start = episode.events[0].closest_waypoint_index
        actual_finish = episode.events[-1].closest_waypoint_index

        # This logic is only for finish >= start    # the opposite is TODO (i.e. crosing start line)
        assert(finish >= start)

        if actual_start <= start and actual_finish >= finish:
            return True

        if actual_finish >= finish and actual_start > actual_finish:
            return True

        if actual_start > actual_finish and actual_start <= start:
            return True

        return False