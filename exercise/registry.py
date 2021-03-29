# from .base import Badge
#
#
# class BadgeCache:
#     def __int__(self):
#         self._event_registry = {}
#         self._registry = {}
#
#     def register(self, badge):
#         assert issubclass(badge, Badge)
#         badge = badge()
#         self._registry[badge.slug] = badge
#         for event in badge.events:
#             self._event_registry.setdefault(event, []).append(badge)
#
#     def possibly_award_badge(self, event, **state):
#         if event in self._event_registry:
#             for badge in self._event_registry[event]:
#                 badge.possibly_award(**state)
#
#
# badges = BadgeCache()
