# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cloudasr/shared/cloudasr/messages/messages.proto

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
  name='cloudasr/shared/cloudasr/messages/messages.proto',
  package='cloudasr.messages',
  serialized_pb=_b('\n0cloudasr/shared/cloudasr/messages/messages.proto\x12\x11\x63loudasr.messages\"\x9e\x01\n\x10HeartbeatMessage\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x02(\t\x12\r\n\x05model\x18\x02 \x02(\t\x12:\n\x06status\x18\x03 \x02(\x0e\x32*.cloudasr.messages.HeartbeatMessage.Status\".\n\x06Status\x12\t\n\x05READY\x10\x00\x12\x0b\n\x07WORKING\x10\x01\x12\x0c\n\x08\x46INISHED\x10\x02\"\xa6\x01\n\x13WorkerStatusMessage\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x02(\t\x12\r\n\x05model\x18\x02 \x02(\t\x12=\n\x06status\x18\x03 \x02(\x0e\x32-.cloudasr.messages.WorkerStatusMessage.Status\x12\x0c\n\x04time\x18\x04 \x02(\x05\"\"\n\x06Status\x12\x0b\n\x07WAITING\x10\x00\x12\x0b\n\x07WORKING\x10\x01\"%\n\x14WorkerRequestMessage\x12\r\n\x05model\x18\x01 \x02(\t\"\x8b\x01\n\x15MasterResponseMessage\x12?\n\x06status\x18\x01 \x02(\x0e\x32/.cloudasr.messages.MasterResponseMessage.Status\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\" \n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\t\n\x05\x45RROR\x10\x01\"\xd8\x01\n\x19RecognitionRequestMessage\x12\'\n\x02id\x18\x01 \x02(\x0b\x32\x1b.cloudasr.messages.UniqueID\x12?\n\x04type\x18\x02 \x02(\x0e\x32\x31.cloudasr.messages.RecognitionRequestMessage.Type\x12\x0c\n\x04\x62ody\x18\x03 \x02(\x0c\x12\x10\n\x08has_next\x18\x04 \x01(\x08\x12\x12\n\nframe_rate\x18\x05 \x01(\x05\"\x1d\n\x04Type\x12\t\n\x05\x42\x41TCH\x10\x00\x12\n\n\x06ONLINE\x10\x01\"5\n\x0b\x41lternative\x12\x12\n\ntranscript\x18\x01 \x02(\t\x12\x12\n\nconfidence\x18\x02 \x02(\x02\"\xb1\x01\n\x0eResultsMessage\x12\x38\n\x06status\x18\x01 \x02(\x0e\x32(.cloudasr.messages.ResultsMessage.Status\x12\r\n\x05\x66inal\x18\x02 \x01(\x08\x12\x34\n\x0c\x61lternatives\x18\x03 \x03(\x0b\x32\x1e.cloudasr.messages.Alternative\" \n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\t\n\x05\x45RROR\x10\x01\"(\n\x08UniqueID\x12\r\n\x05lower\x18\x01 \x02(\x04\x12\r\n\x05upper\x18\x02 \x02(\x04')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_HEARTBEATMESSAGE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='cloudasr.messages.HeartbeatMessage.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='READY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORKING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINISHED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=184,
  serialized_end=230,
)
_sym_db.RegisterEnumDescriptor(_HEARTBEATMESSAGE_STATUS)

_WORKERSTATUSMESSAGE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='cloudasr.messages.WorkerStatusMessage.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WAITING', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORKING', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=365,
  serialized_end=399,
)
_sym_db.RegisterEnumDescriptor(_WORKERSTATUSMESSAGE_STATUS)

_MASTERRESPONSEMESSAGE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='cloudasr.messages.MasterResponseMessage.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=548,
  serialized_end=580,
)
_sym_db.RegisterEnumDescriptor(_MASTERRESPONSEMESSAGE_STATUS)

_RECOGNITIONREQUESTMESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='cloudasr.messages.RecognitionRequestMessage.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BATCH', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONLINE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=770,
  serialized_end=799,
)
_sym_db.RegisterEnumDescriptor(_RECOGNITIONREQUESTMESSAGE_TYPE)

_RESULTSMESSAGE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='cloudasr.messages.ResultsMessage.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=548,
  serialized_end=580,
)
_sym_db.RegisterEnumDescriptor(_RESULTSMESSAGE_STATUS)


_HEARTBEATMESSAGE = _descriptor.Descriptor(
  name='HeartbeatMessage',
  full_name='cloudasr.messages.HeartbeatMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='cloudasr.messages.HeartbeatMessage.address', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model', full_name='cloudasr.messages.HeartbeatMessage.model', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='cloudasr.messages.HeartbeatMessage.status', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HEARTBEATMESSAGE_STATUS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=230,
)


_WORKERSTATUSMESSAGE = _descriptor.Descriptor(
  name='WorkerStatusMessage',
  full_name='cloudasr.messages.WorkerStatusMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='cloudasr.messages.WorkerStatusMessage.address', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model', full_name='cloudasr.messages.WorkerStatusMessage.model', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='cloudasr.messages.WorkerStatusMessage.status', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='cloudasr.messages.WorkerStatusMessage.time', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _WORKERSTATUSMESSAGE_STATUS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=399,
)


_WORKERREQUESTMESSAGE = _descriptor.Descriptor(
  name='WorkerRequestMessage',
  full_name='cloudasr.messages.WorkerRequestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model', full_name='cloudasr.messages.WorkerRequestMessage.model', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=401,
  serialized_end=438,
)


_MASTERRESPONSEMESSAGE = _descriptor.Descriptor(
  name='MasterResponseMessage',
  full_name='cloudasr.messages.MasterResponseMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cloudasr.messages.MasterResponseMessage.status', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address', full_name='cloudasr.messages.MasterResponseMessage.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MASTERRESPONSEMESSAGE_STATUS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=441,
  serialized_end=580,
)


_RECOGNITIONREQUESTMESSAGE = _descriptor.Descriptor(
  name='RecognitionRequestMessage',
  full_name='cloudasr.messages.RecognitionRequestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cloudasr.messages.RecognitionRequestMessage.id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='cloudasr.messages.RecognitionRequestMessage.type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='body', full_name='cloudasr.messages.RecognitionRequestMessage.body', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has_next', full_name='cloudasr.messages.RecognitionRequestMessage.has_next', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frame_rate', full_name='cloudasr.messages.RecognitionRequestMessage.frame_rate', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RECOGNITIONREQUESTMESSAGE_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=583,
  serialized_end=799,
)


_ALTERNATIVE = _descriptor.Descriptor(
  name='Alternative',
  full_name='cloudasr.messages.Alternative',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transcript', full_name='cloudasr.messages.Alternative.transcript', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='cloudasr.messages.Alternative.confidence', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=801,
  serialized_end=854,
)


_RESULTSMESSAGE = _descriptor.Descriptor(
  name='ResultsMessage',
  full_name='cloudasr.messages.ResultsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cloudasr.messages.ResultsMessage.status', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='final', full_name='cloudasr.messages.ResultsMessage.final', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alternatives', full_name='cloudasr.messages.ResultsMessage.alternatives', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESULTSMESSAGE_STATUS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=857,
  serialized_end=1034,
)


_UNIQUEID = _descriptor.Descriptor(
  name='UniqueID',
  full_name='cloudasr.messages.UniqueID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lower', full_name='cloudasr.messages.UniqueID.lower', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upper', full_name='cloudasr.messages.UniqueID.upper', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1036,
  serialized_end=1076,
)

_HEARTBEATMESSAGE.fields_by_name['status'].enum_type = _HEARTBEATMESSAGE_STATUS
_HEARTBEATMESSAGE_STATUS.containing_type = _HEARTBEATMESSAGE
_WORKERSTATUSMESSAGE.fields_by_name['status'].enum_type = _WORKERSTATUSMESSAGE_STATUS
_WORKERSTATUSMESSAGE_STATUS.containing_type = _WORKERSTATUSMESSAGE
_MASTERRESPONSEMESSAGE.fields_by_name['status'].enum_type = _MASTERRESPONSEMESSAGE_STATUS
_MASTERRESPONSEMESSAGE_STATUS.containing_type = _MASTERRESPONSEMESSAGE
_RECOGNITIONREQUESTMESSAGE.fields_by_name['id'].message_type = _UNIQUEID
_RECOGNITIONREQUESTMESSAGE.fields_by_name['type'].enum_type = _RECOGNITIONREQUESTMESSAGE_TYPE
_RECOGNITIONREQUESTMESSAGE_TYPE.containing_type = _RECOGNITIONREQUESTMESSAGE
_RESULTSMESSAGE.fields_by_name['status'].enum_type = _RESULTSMESSAGE_STATUS
_RESULTSMESSAGE.fields_by_name['alternatives'].message_type = _ALTERNATIVE
_RESULTSMESSAGE_STATUS.containing_type = _RESULTSMESSAGE
DESCRIPTOR.message_types_by_name['HeartbeatMessage'] = _HEARTBEATMESSAGE
DESCRIPTOR.message_types_by_name['WorkerStatusMessage'] = _WORKERSTATUSMESSAGE
DESCRIPTOR.message_types_by_name['WorkerRequestMessage'] = _WORKERREQUESTMESSAGE
DESCRIPTOR.message_types_by_name['MasterResponseMessage'] = _MASTERRESPONSEMESSAGE
DESCRIPTOR.message_types_by_name['RecognitionRequestMessage'] = _RECOGNITIONREQUESTMESSAGE
DESCRIPTOR.message_types_by_name['Alternative'] = _ALTERNATIVE
DESCRIPTOR.message_types_by_name['ResultsMessage'] = _RESULTSMESSAGE
DESCRIPTOR.message_types_by_name['UniqueID'] = _UNIQUEID

HeartbeatMessage = _reflection.GeneratedProtocolMessageType('HeartbeatMessage', (_message.Message,), dict(
  DESCRIPTOR = _HEARTBEATMESSAGE,
  __module__ = 'cloudasr.shared.cloudasr.messages.messages_pb2'
  # @@protoc_insertion_point(class_scope:cloudasr.messages.HeartbeatMessage)
  ))
_sym_db.RegisterMessage(HeartbeatMessage)

WorkerStatusMessage = _reflection.GeneratedProtocolMessageType('WorkerStatusMessage', (_message.Message,), dict(
  DESCRIPTOR = _WORKERSTATUSMESSAGE,
  __module__ = 'cloudasr.shared.cloudasr.messages.messages_pb2'
  # @@protoc_insertion_point(class_scope:cloudasr.messages.WorkerStatusMessage)
  ))
_sym_db.RegisterMessage(WorkerStatusMessage)

WorkerRequestMessage = _reflection.GeneratedProtocolMessageType('WorkerRequestMessage', (_message.Message,), dict(
  DESCRIPTOR = _WORKERREQUESTMESSAGE,
  __module__ = 'cloudasr.shared.cloudasr.messages.messages_pb2'
  # @@protoc_insertion_point(class_scope:cloudasr.messages.WorkerRequestMessage)
  ))
_sym_db.RegisterMessage(WorkerRequestMessage)

MasterResponseMessage = _reflection.GeneratedProtocolMessageType('MasterResponseMessage', (_message.Message,), dict(
  DESCRIPTOR = _MASTERRESPONSEMESSAGE,
  __module__ = 'cloudasr.shared.cloudasr.messages.messages_pb2'
  # @@protoc_insertion_point(class_scope:cloudasr.messages.MasterResponseMessage)
  ))
_sym_db.RegisterMessage(MasterResponseMessage)

RecognitionRequestMessage = _reflection.GeneratedProtocolMessageType('RecognitionRequestMessage', (_message.Message,), dict(
  DESCRIPTOR = _RECOGNITIONREQUESTMESSAGE,
  __module__ = 'cloudasr.shared.cloudasr.messages.messages_pb2'
  # @@protoc_insertion_point(class_scope:cloudasr.messages.RecognitionRequestMessage)
  ))
_sym_db.RegisterMessage(RecognitionRequestMessage)

Alternative = _reflection.GeneratedProtocolMessageType('Alternative', (_message.Message,), dict(
  DESCRIPTOR = _ALTERNATIVE,
  __module__ = 'cloudasr.shared.cloudasr.messages.messages_pb2'
  # @@protoc_insertion_point(class_scope:cloudasr.messages.Alternative)
  ))
_sym_db.RegisterMessage(Alternative)

ResultsMessage = _reflection.GeneratedProtocolMessageType('ResultsMessage', (_message.Message,), dict(
  DESCRIPTOR = _RESULTSMESSAGE,
  __module__ = 'cloudasr.shared.cloudasr.messages.messages_pb2'
  # @@protoc_insertion_point(class_scope:cloudasr.messages.ResultsMessage)
  ))
_sym_db.RegisterMessage(ResultsMessage)

UniqueID = _reflection.GeneratedProtocolMessageType('UniqueID', (_message.Message,), dict(
  DESCRIPTOR = _UNIQUEID,
  __module__ = 'cloudasr.shared.cloudasr.messages.messages_pb2'
  # @@protoc_insertion_point(class_scope:cloudasr.messages.UniqueID)
  ))
_sym_db.RegisterMessage(UniqueID)


# @@protoc_insertion_point(module_scope)
