from redis.asyncio import Redis


def put_dict_in_order(data: dict):
    return {k: v for k, v in sorted(map(lambda x: (x[0], int(x[1])), data.items()), key=lambda x: x[-1])}


async def get_analytics(client: Redis):
    obj = await client.hgetall('analytics')

    obj['total_requests'] = int(obj.get('total_requests', 0))
    obj['locations'] = put_dict_in_order(await client.hgetall('locations') or {})
    obj['categories'] = put_dict_in_order(await client.hgetall('categories') or {})

    return obj


async def add_updates(client: Redis, location_id: int, category_id: int):
    await update_total_requests(client)
    await update_locations_requests(client, location_id)
    await update_categories_requests(client, category_id)


async def update_total_requests(client: Redis):
    if not await client.hgetall('analytics'):
        await client.hset('analytics', mapping={"total_requests": 0})

    await client.hincrby(name="analytics", key="total_requests", amount=1)


async def update_locations_requests(client: Redis, location_id: int):
    if not await client.hget('locations', '-1'):
        await client.hset('locations', mapping={'-1': -1})

    if not await client.hget('locations', str(location_id)):
        await client.hset('locations', key=str(location_id), value=0)
    await client.hincrby(name="locations", key=str(location_id), amount=1)


async def update_categories_requests(client: Redis, category_id: int):
    if not await client.hget('categories', '-1'):
        await client.hset('categories', mapping={'-1': -1})

    if not await client.hget('categories', str(category_id)):
        await client.hset('categories', key=str(category_id), value=0)
    await client.hincrby(name="categories", key=str(category_id), amount=1)
