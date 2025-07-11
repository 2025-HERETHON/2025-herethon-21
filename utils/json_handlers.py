from django.db import models

class JSONIntListHandler:
    """
    정수 리스트 데이터를 저장하는 JSON 필드를 관리합니다.
    """
    def __init__(self, instance: models.Model, field_name: str):
        """
        Args:
            instance (django.db.models.Model): 모델 인스턴스
            field_name (str): JSON 필드 이름 (예: 'exercise_goal')
        """
        self.instance = instance
        self.field_name = field_name

    def _get_values(self) -> list:
        return getattr(self.instance, self.field_name) or []

    def _set_values(self, values: list[int]):
        setattr(self.instance, self.field_name, values)

    def set(self, items: list[int], save: bool = True):
        self._set_values(items)
        if save:
            self.instance.save()

    def has(self, item: int):
        return item in self.get_int_values()

    def add(self, item: int, save: bool = True):
        self._get_values().append(item)
        if save:
            self.instance.save()

    def add_unique(self, item: int, save: bool = True):
        if not self.has(item):
            self._get_values().append(item)
            if save:
                self.instance.save()
            return True
        return False

    def remove(self, item: int, save: bool = True):
        has_item = self.has(item)
        while self.has(item):
            self._get_values().remove(item)
        if has_item and save:
            self.instance.save()
        return has_item

    def get_int_values(self) -> list[int]:
        """
        필드에 저장된 값을 정수 리스트로 안전하게 반환합니다.
        문자열 숫자도 자동으로 int로 변환됩니다.
        """
        return [int(v) for v in self._get_values()]


class JSONIntChoicesListHandler(JSONIntListHandler):
    """
    IntegerChoices 리스트 데이터를 저장하는 JSON 필드를 관리합니다.
    """
    def __init__(self, instance: models.Model, field_name: str, integer_choices_class: models.IntegerChoices):
        super().__init__(instance, field_name)
        self.integer_choices_class = integer_choices_class

    def _validate(self, value: int):
        try:
            self.integer_choices_class(value)
        except ValueError:
            raise ValueError(
                f"{value} 은/는 {self.integer_choices_class.__name__} 클래스에 정의되지 않은 값입니다.\n"
                f"유효한 값: {[f'{choice.value}({choice.label})' for choice in self.integer_choices_class]}"
            )

    def get_display_names(self) -> list[str]:
        """
        원래 메서드: 변환 없이 저장된 값을 IntegerChoices의 label로 반환합니다.
        주의: 문자열이 저장된 경우 오류 발생 가능
        """
        return [
            self.integer_choices_class(item).label
            for item in self._get_values()
        ]

    def get_display_names_safe(self) -> list[str]:
        """
        🆕 안전 버전: 문자열 숫자도 변환 후 IntegerChoices label로 매핑합니다.
        예: ["2", "4"] → ["건강 관리", "근력 강화"]
        """
        return [
            self.integer_choices_class(item).label
            for item in self.get_int_values()
        ]

    def set(self, items, save=True):
        for item in items:
            self._validate(item)
        return super().set(items, save)

    def add(self, item, save=True):
        self._validate(item)
        return super().add(item, save)

    def add_unique(self, item, save=True):
        self._validate(item)
        return super().add_unique(item, save)

    def remove(self, item, save=True):
        self._validate(item)
        return super().remove(item, save)
