import pytest
from startupevents.profiles.models import UserProfile
from startupevents.customuser.models import User

pytestmark = pytest.mark.django_db


def test_profile_model():
    user_ = User.objects.create_user(
        email='f@F.com', password='abc', first_name="F", last_name='B')
    user_profile = UserProfile.objects.create(
        user=user_, mobile="1234567890", work_location="JUST ANOTHER LOCATION", work_experience=4.2)
    assert user_profile.user == user_
    assert user_profile.mobile == "1234567890"
    assert user_profile.work_location == "JUST ANOTHER LOCATION"
    assert user_profile.work_experience == 4.2
    assert str(user_profile) == "{} {}".format(user_.id, user_.email)
