# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages_robocup_ssl_geometry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages_robocup_ssl_geometry.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n#messages_robocup_ssl_geometry.proto\" \n\x08Vector2f\x12\t\n\x01x\x18\x01 \x02(\x02\x12\t\n\x01y\x18\x02 \x02(\x02\"e\n\x14SSL_FieldLineSegment\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x15\n\x02p1\x18\x02 \x02(\x0b\x32\t.Vector2f\x12\x15\n\x02p2\x18\x03 \x02(\x0b\x32\t.Vector2f\x12\x11\n\tthickness\x18\x04 \x02(\x02\"y\n\x13SSL_FieldCicularArc\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x19\n\x06\x63\x65nter\x18\x02 \x02(\x0b\x32\t.Vector2f\x12\x0e\n\x06radius\x18\x03 \x02(\x02\x12\n\n\x02\x61\x31\x18\x04 \x02(\x02\x12\n\n\x02\x61\x32\x18\x05 \x02(\x02\x12\x11\n\tthickness\x18\x06 \x02(\x02\"\xd8\x01\n\x15SSL_GeometryFieldSize\x12\x14\n\x0c\x66ield_length\x18\x01 \x02(\x05\x12\x13\n\x0b\x66ield_width\x18\x02 \x02(\x05\x12\x12\n\ngoal_width\x18\x03 \x02(\x05\x12\x12\n\ngoal_depth\x18\x04 \x02(\x05\x12\x16\n\x0e\x62oundary_width\x18\x05 \x02(\x05\x12*\n\x0b\x66ield_lines\x18\x06 \x03(\x0b\x32\x15.SSL_FieldLineSegment\x12(\n\nfield_arcs\x18\x07 \x03(\x0b\x32\x14.SSL_FieldCicularArc\"\xc9\x02\n\x1dSSL_GeometryCameraCalibration\x12\x11\n\tcamera_id\x18\x01 \x02(\r\x12\x14\n\x0c\x66ocal_length\x18\x02 \x02(\x02\x12\x19\n\x11principal_point_x\x18\x03 \x02(\x02\x12\x19\n\x11principal_point_y\x18\x04 \x02(\x02\x12\x12\n\ndistortion\x18\x05 \x02(\x02\x12\n\n\x02q0\x18\x06 \x02(\x02\x12\n\n\x02q1\x18\x07 \x02(\x02\x12\n\n\x02q2\x18\x08 \x02(\x02\x12\n\n\x02q3\x18\t \x02(\x02\x12\n\n\x02tx\x18\n \x02(\x02\x12\n\n\x02ty\x18\x0b \x02(\x02\x12\n\n\x02tz\x18\x0c \x02(\x02\x12\x1f\n\x17\x64\x65rived_camera_world_tx\x18\r \x01(\x02\x12\x1f\n\x17\x64\x65rived_camera_world_ty\x18\x0e \x01(\x02\x12\x1f\n\x17\x64\x65rived_camera_world_tz\x18\x0f \x01(\x02\"h\n\x10SSL_GeometryData\x12%\n\x05\x66ield\x18\x01 \x02(\x0b\x32\x16.SSL_GeometryFieldSize\x12-\n\x05\x63\x61lib\x18\x02 \x03(\x0b\x32\x1e.SSL_GeometryCameraCalibration')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_VECTOR2F = _descriptor.Descriptor(
  name='Vector2f',
  full_name='Vector2f',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='Vector2f.x', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='Vector2f.y', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=71,
)


_SSL_FIELDLINESEGMENT = _descriptor.Descriptor(
  name='SSL_FieldLineSegment',
  full_name='SSL_FieldLineSegment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='SSL_FieldLineSegment.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='p1', full_name='SSL_FieldLineSegment.p1', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='p2', full_name='SSL_FieldLineSegment.p2', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thickness', full_name='SSL_FieldLineSegment.thickness', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=174,
)


_SSL_FIELDCICULARARC = _descriptor.Descriptor(
  name='SSL_FieldCicularArc',
  full_name='SSL_FieldCicularArc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='SSL_FieldCicularArc.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='center', full_name='SSL_FieldCicularArc.center', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='radius', full_name='SSL_FieldCicularArc.radius', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='a1', full_name='SSL_FieldCicularArc.a1', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='a2', full_name='SSL_FieldCicularArc.a2', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thickness', full_name='SSL_FieldCicularArc.thickness', index=5,
      number=6, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=176,
  serialized_end=297,
)


_SSL_GEOMETRYFIELDSIZE = _descriptor.Descriptor(
  name='SSL_GeometryFieldSize',
  full_name='SSL_GeometryFieldSize',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field_length', full_name='SSL_GeometryFieldSize.field_length', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field_width', full_name='SSL_GeometryFieldSize.field_width', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='goal_width', full_name='SSL_GeometryFieldSize.goal_width', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='goal_depth', full_name='SSL_GeometryFieldSize.goal_depth', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boundary_width', full_name='SSL_GeometryFieldSize.boundary_width', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field_lines', full_name='SSL_GeometryFieldSize.field_lines', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field_arcs', full_name='SSL_GeometryFieldSize.field_arcs', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=300,
  serialized_end=516,
)


_SSL_GEOMETRYCAMERACALIBRATION = _descriptor.Descriptor(
  name='SSL_GeometryCameraCalibration',
  full_name='SSL_GeometryCameraCalibration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='camera_id', full_name='SSL_GeometryCameraCalibration.camera_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='focal_length', full_name='SSL_GeometryCameraCalibration.focal_length', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='principal_point_x', full_name='SSL_GeometryCameraCalibration.principal_point_x', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='principal_point_y', full_name='SSL_GeometryCameraCalibration.principal_point_y', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distortion', full_name='SSL_GeometryCameraCalibration.distortion', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='q0', full_name='SSL_GeometryCameraCalibration.q0', index=5,
      number=6, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='q1', full_name='SSL_GeometryCameraCalibration.q1', index=6,
      number=7, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='q2', full_name='SSL_GeometryCameraCalibration.q2', index=7,
      number=8, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='q3', full_name='SSL_GeometryCameraCalibration.q3', index=8,
      number=9, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tx', full_name='SSL_GeometryCameraCalibration.tx', index=9,
      number=10, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ty', full_name='SSL_GeometryCameraCalibration.ty', index=10,
      number=11, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tz', full_name='SSL_GeometryCameraCalibration.tz', index=11,
      number=12, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='derived_camera_world_tx', full_name='SSL_GeometryCameraCalibration.derived_camera_world_tx', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='derived_camera_world_ty', full_name='SSL_GeometryCameraCalibration.derived_camera_world_ty', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='derived_camera_world_tz', full_name='SSL_GeometryCameraCalibration.derived_camera_world_tz', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=519,
  serialized_end=848,
)


_SSL_GEOMETRYDATA = _descriptor.Descriptor(
  name='SSL_GeometryData',
  full_name='SSL_GeometryData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field', full_name='SSL_GeometryData.field', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='calib', full_name='SSL_GeometryData.calib', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=850,
  serialized_end=954,
)

_SSL_FIELDLINESEGMENT.fields_by_name['p1'].message_type = _VECTOR2F
_SSL_FIELDLINESEGMENT.fields_by_name['p2'].message_type = _VECTOR2F
_SSL_FIELDCICULARARC.fields_by_name['center'].message_type = _VECTOR2F
_SSL_GEOMETRYFIELDSIZE.fields_by_name['field_lines'].message_type = _SSL_FIELDLINESEGMENT
_SSL_GEOMETRYFIELDSIZE.fields_by_name['field_arcs'].message_type = _SSL_FIELDCICULARARC
_SSL_GEOMETRYDATA.fields_by_name['field'].message_type = _SSL_GEOMETRYFIELDSIZE
_SSL_GEOMETRYDATA.fields_by_name['calib'].message_type = _SSL_GEOMETRYCAMERACALIBRATION
DESCRIPTOR.message_types_by_name['Vector2f'] = _VECTOR2F
DESCRIPTOR.message_types_by_name['SSL_FieldLineSegment'] = _SSL_FIELDLINESEGMENT
DESCRIPTOR.message_types_by_name['SSL_FieldCicularArc'] = _SSL_FIELDCICULARARC
DESCRIPTOR.message_types_by_name['SSL_GeometryFieldSize'] = _SSL_GEOMETRYFIELDSIZE
DESCRIPTOR.message_types_by_name['SSL_GeometryCameraCalibration'] = _SSL_GEOMETRYCAMERACALIBRATION
DESCRIPTOR.message_types_by_name['SSL_GeometryData'] = _SSL_GEOMETRYDATA

Vector2f = _reflection.GeneratedProtocolMessageType('Vector2f', (_message.Message,), dict(
  DESCRIPTOR = _VECTOR2F,
  __module__ = 'messages_robocup_ssl_geometry_pb2'
  # @@protoc_insertion_point(class_scope:Vector2f)
  ))
_sym_db.RegisterMessage(Vector2f)

SSL_FieldLineSegment = _reflection.GeneratedProtocolMessageType('SSL_FieldLineSegment', (_message.Message,), dict(
  DESCRIPTOR = _SSL_FIELDLINESEGMENT,
  __module__ = 'messages_robocup_ssl_geometry_pb2'
  # @@protoc_insertion_point(class_scope:SSL_FieldLineSegment)
  ))
_sym_db.RegisterMessage(SSL_FieldLineSegment)

SSL_FieldCicularArc = _reflection.GeneratedProtocolMessageType('SSL_FieldCicularArc', (_message.Message,), dict(
  DESCRIPTOR = _SSL_FIELDCICULARARC,
  __module__ = 'messages_robocup_ssl_geometry_pb2'
  # @@protoc_insertion_point(class_scope:SSL_FieldCicularArc)
  ))
_sym_db.RegisterMessage(SSL_FieldCicularArc)

SSL_GeometryFieldSize = _reflection.GeneratedProtocolMessageType('SSL_GeometryFieldSize', (_message.Message,), dict(
  DESCRIPTOR = _SSL_GEOMETRYFIELDSIZE,
  __module__ = 'messages_robocup_ssl_geometry_pb2'
  # @@protoc_insertion_point(class_scope:SSL_GeometryFieldSize)
  ))
_sym_db.RegisterMessage(SSL_GeometryFieldSize)

SSL_GeometryCameraCalibration = _reflection.GeneratedProtocolMessageType('SSL_GeometryCameraCalibration', (_message.Message,), dict(
  DESCRIPTOR = _SSL_GEOMETRYCAMERACALIBRATION,
  __module__ = 'messages_robocup_ssl_geometry_pb2'
  # @@protoc_insertion_point(class_scope:SSL_GeometryCameraCalibration)
  ))
_sym_db.RegisterMessage(SSL_GeometryCameraCalibration)

SSL_GeometryData = _reflection.GeneratedProtocolMessageType('SSL_GeometryData', (_message.Message,), dict(
  DESCRIPTOR = _SSL_GEOMETRYDATA,
  __module__ = 'messages_robocup_ssl_geometry_pb2'
  # @@protoc_insertion_point(class_scope:SSL_GeometryData)
  ))
_sym_db.RegisterMessage(SSL_GeometryData)


# @@protoc_insertion_point(module_scope)
