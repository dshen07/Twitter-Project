def invalidate_following_cache(sender, instance, **kwargs):
    from friendships.services import FriendshipService
    FriendshipService.invalidate_following_cache(instance.from_user.id)