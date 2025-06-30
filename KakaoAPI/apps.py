from django.apps import AppConfig


class KakaoapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'KakaoAPI'

    def ready(self):
        from allauth.socialaccount.models import SocialApp
        from django.conf import settings
        from django.contrib.sites.models import Site
        from django.db.utils import OperationalError, ProgrammingError

        try:
            # 기본 SITE_ID
            site = Site.objects.get(id=settings.SITE_ID)

            # 카카오
            kakao, created = SocialApp.objects.get_or_create(
                provider="kakao",
                defaults={
                    "name": "Kakao",
                    "client_id": settings.KAKAO_CLIENT_ID,
                    "secret": settings.KAKAO_SECRET,
                }
            )
            if not created:
                kakao.client_id = settings.KAKAO_CLIENT_ID
                kakao.secret = settings.KAKAO_SECRET
                kakao.save()
            kakao.sites.set([site])

        except (OperationalError, ProgrammingError):
            # migrate 하기 전에는 테이블이 없을 수 있으므로 무시
            pass
