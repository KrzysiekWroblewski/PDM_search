class Item:
    def __init__(self, id, revision=None, description=None, drawing_Number=None, material=None, quantity=0, mirror_quantity=0):
        self.id = id
        self.revision = revision
        self.description = description
        self.drawing_Number = drawing_Number
        self.material = material
        self.quantity = quantity
        self.mirror_quantity = mirror_quantity

    def __str__(self):
        return str(self.id)

    def print_item_values(self):
        values = (self.id, self.revision, self.description, self.drawing_Number,
                  self.material, self.quantity, self.mirror_quantity)
        return values
