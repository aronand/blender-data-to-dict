class MockModifier:
    def __init__(self, type_name: str):
        self.type = type_name


class MockMesh:
    def __init__(self, name: str):
        self.name = name


class MockObject:
    def __init__(self, name: str, obj_type: str):
        self.name = name
        self.type = obj_type
        self.data: MockMesh | None = None
        self.modifiers = []
        self.material_slots = []


class MockMaterialSlot:
    def __init__(self, name: str):
        self.name = name
