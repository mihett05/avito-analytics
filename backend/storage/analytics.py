from redis.asyncio import Redis


async def get_storage_conf(client: Redis):
    pass


storage_example = {
    "baseline": 0,
    "discounts": set(),

    "analytics": {
        "meta": {
            'total_requests': 0,
            'matrix_requests': 0,
            'locations_requests': 0,
            'categories_requests': 0,
            'price_target_requests': 0,
        },
        'tables': {
            'prices': {'rows': 0, 'updates': 0, 'deletions': 0, 'creations': 0},
            'matrices': {'rows': 0, 'updates': 0, 'deletions': 0, 'creations': 0},
            'locations': {'rows': 0, 'updates': 0, 'deletions': 0, 'creations': 0},
            'categories': {'rows': 0, 'updates': 0, 'deletions': 0, 'creations': 0}
        }
    }
}
