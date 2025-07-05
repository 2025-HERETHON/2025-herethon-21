from django.db import models

class JSONIntListHandler:
    """
    정수 리스트 데이터를 저장하는 JSON 필드를 관리합니다.
    """
    def __init__(self, instance: models.Model, field_name:str):
        """
        Args:
            instance(django.db.models.Model): 모델 인스턴스
            field_name(str): JSON 필드 이름 (예: 'exercise_goal')
        """
        self.instance = instance
        self.field_name = field_name
    
    def _get_values(self) -> list[int]:
        return getattr(self.instance, self.field_name)
    
    def _set_values(self, values:list[int]):
        setattr(self.instance, self.field_name, values)

    def set(self, items:list[int], save:bool=True):
        """
        전체 데이터를 덮어씁니다.
        Args:
            items(list[int]): 덮어쓸 데이터
            save(bool): 저장 여부 (기본값: True)
        """
        self._set_values(items)
        if save: self.instance.save()
    
    def has(self, item:int):
        """
        항목이 존재하는지 여부를 반환합니다.
        Args:
            item(int): 확인할 항목
        """
        return item in self._get_values()
    
    def add(self, item:int, save:bool=True):
        """
        항목을 추가합니다. 중복 여부를 확인하지 않습니다.
        Args:
            item(int): 추가할 항목
            save(bool): 저장 여부 (기본값: True)
        """
        self._get_values().append(item)
        if save: self.instance.save()
    
    def add_unique(self, item:int, save:bool=True):
        """
        중복되지 않는 경우에만 항목을 추가합니다.
        Args:
            item(int): 추가할 항목
            save(bool): 저장 여부 (기본값: True)
        Returns:
            bool: 추가한 경우 True, 이미 존재하는 경우 False
        """
        if not self.has(item):
            self._get_values().append(item)
            if save: self.instance.save()
            return True
        return False
    
    def remove(self, item:int, save:bool=True):
        """
        항목과 일치하는 모든 값을 삭제합니다.
        Args:
            item(int): 삭제할 항목
            save(bool): 저장 여부 (기본값: True)
        Returns:
            bool: 삭제한 경우 True, 이미 존재하지 않는 경우 False
        """
        has_item = self.has(item)
        while self.has(item):
            self._get_values().remove(item)
        if has_item:
            if save: self.instance.save()
        return has_item

class JSONIntChoicesListHandler(JSONIntListHandler):
    """
    IntegerChoices 리스트 데이터를 저장하는 JSON 필드를 관리합니다.
    """
    def __init__(self, instance:models.Model, field_name:str, integer_choices_class:models.IntegerChoices):
        """
        Args:
            instance(django.db.models.Model): 모델 인스턴스
            field_name(str): JSON 필드 이름 (예: 'exercise_goal')
            integer_choices_class(django.db.models.IntegerChoices): IntegerChoices를 상속한 클래스
        """
        super().__init__(instance, field_name)
        self.integer_choices_class = integer_choices_class
    
    def _validate(self, value:int):
        """
        IntegerChoices에 정의된 값인지 확인합니다.
        """
        try:
            self.integer_choices_class(value)
        except ValueError:
            raise ValueError(f"""
                {value} 은/는 {self.integer_choices_class.__name__} 클래스에 정의되지 않은 값입니다.
                유효한 값: {[f"{choice.value}({choice.label})" for choice in self.integer_choices_class]}
            """)
        
    def get_display_names(self) -> list[str]:
        """
        전체 데이터를 대응하는 IntegerChoices의 label로 변환하여 반환합니다. (예: [2,4] → ['건강 관리','근력 강화'])
        Returns:
            list[str]: IntegerChoices의 label로 변환한 리스트 (예: ['건강 관리','근력 강화'])
        """
        return [self.integer_choices_class(item).label for item in self._get_values()]
   
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