from .. import Node

# Joint
class Joint(Node):
    class_name = "Joint"
    length = 64
    fields = [
        ('name', 'string'),
        ('flags', 'uint'),
        ('child', 'Joint'),
        ('next', 'Joint'),
        ('u', 'uint'),
        ('rotation', 'vec3'),
        ('scale', 'vec3'),
        ('position', 'vec3'),
        ('inverse_bind', 'uint'),
        ('robject', 'RObject')
    ]

    # Parse struct from binary file.
    @classmethod
    def fromBinary(cls, parser, address):
        return parser.parseStruct(cls, address)

    # Tells the builder how to write this node's data to the binary file.
    # Returns the offset the builder was at before it started writing its own data.
    def writeBinary(self, builder):
        return builder.writeStruct(self)

    # Make approximation HSD struct from blender data.
    @classmethod
    def fromBlender(cls, blender_obj):
        pass

    # Make approximation Blender object from HSD data.
    def toBlender(self, context):
        pass