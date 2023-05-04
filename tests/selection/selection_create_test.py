import pytest
from rest_framework import status

from tests.factories import AdFactory


@pytest.mark.django_db
def test_selection_create(client, user_with_access_token):
    user, access_token = user_with_access_token
    ad_list = AdFactory.create_batch(8)
    data = {
        'name': 'test_selection',
        'items': [ad.pk for ad in ad_list[1:5]]
    }

    expected_data = {
        'id': 1,
        'owner': user.username,
        'name': 'test_selection',
        'items': [ad.pk for ad in ad_list[1:5]]
    }

    response = client.post('/selection/', data=data, HTTP_AUTHORIZATION=f'Bearer {access_token}')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == expected_data
