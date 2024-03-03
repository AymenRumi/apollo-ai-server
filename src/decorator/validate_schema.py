from functools import wraps


def pydantic(pydantic_model):
    def decorator(func):
        @wraps(func)
        async def wrapper(self, sid, data):
            try:
                validated_data = pydantic_model(**data)
                return await func(self, sid, validated_data)
            except Exception as e:
                print(f"Validation error: {e}")
                # await self.emit('error', {'error': 'Invalid data format'}, to=sid)

        return wrapper

    return decorator
