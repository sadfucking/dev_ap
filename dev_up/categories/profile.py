from dev_up import models
from dev_up.categories.base import BaseAPICategories


class ProfileAPICategories(BaseAPICategories):

    def get(self, user_id: int = None, key: str = None, **kwargs) -> models.ProfileGet:
        """Получает информацию о профиле DEV-UP"""
        return self.api.make_request(
            method='profile.get',
            data=dict(user_id=user_id, key=key, **kwargs),
            dataclass=models.ProfileGet
        )

    def buy_premium(self, key: str = None, **kwargs) -> models.ProfileBuyPremium:
        """Получение premium статуса"""
        return self.api.make_request(
            method='profile.buyPremium',
            data=dict(key=key, **kwargs),
            dataclass=models.ProfileBuyPremium
        )

    def buy_limit(self, amount: int, key: str = None, **kwargs) -> models.ProfileBuyLimit:
        """Покупка лимита"""
        return self.api.make_request(
            method='profile.buyLimit',
            data=dict(amount=amount, key=key, **kwargs),
            dataclass=models.ProfileBuyLimit
        )

    def get_balance_link(self, amount: int, vk: int, key: str = None, **kwargs) -> models.ProfileGetBalanceLink:
        """Получение ссылки на пополнение баланса"""
        return self.api.make_request(
            method='profile.getBalanceLink',
            data=dict(amount=amount, vk=vk, key=key, **kwargs),
            dataclass=models.ProfileGetBalanceLink
        )

    def set_key(self) -> models.ProfileSetKey:
        """Обнуление ключа доступа"""
        return self.api.make_request(
            method='profile.setKey',
            data=dict(),
            dataclass=models.ProfileSetKey
        )

    async def get_async(self, key: str = None, **kwargs) -> models.ProfileGet:
        """Получает информацию о профиле DEV-UP"""
        return await self.api.make_request_async(
            method='profile.get',
            data=dict(key=key, **kwargs),
            dataclass=models.ProfileGet
        )

    async def buy_premium_async(self, key: str = None, **kwargs) -> models.ProfileBuyPremium:
        """Получение premium статуса"""
        return await self.api.make_request_async(
            method='profile.buyPremium',
            data=dict(key=key, **kwargs),
            dataclass=models.ProfileBuyPremium
        )

    async def buy_limit_async(self, amount: int, key: str = None, **kwargs) -> models.ProfileBuyLimit:
        """Покупка лимита"""
        return await self.api.make_request_async(
            method='profile.buyLimit',
            data=dict(amount=amount, key=key, **kwargs),
            dataclass=models.ProfileBuyLimit
        )

    async def get_balance_link_async(
            self, amount: int, vk: int, key: str = None, **kwargs
    ) -> models.ProfileGetBalanceLink:
        """Получение ссылки на пополнение баланса"""
        return await self.api.make_request_async(
            method='profile.getBalanceLink',
            data=dict(amount=amount, vk=vk, key=key, **kwargs),
            dataclass=models.ProfileGetBalanceLink
        )

    async def set_key_async(self, **kwargs) -> models.ProfileSetKey:
        """Обнуление ключа доступа"""
        return await self.api.make_request_async(
            method='profile.setKey',
            data=dict(**kwargs),
            dataclass=models.ProfileSetKey
        )
