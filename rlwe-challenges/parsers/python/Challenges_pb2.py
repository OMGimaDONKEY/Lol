# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Challenges.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Lol_pb2
import RLWE_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Challenges.proto',
  package='',
  serialized_pb=_b('\n\x10\x43hallenges.proto\x1a\tLol.proto\x1a\nRLWE.proto\"S\n\nContParams\x12\t\n\x01m\x18\x01 \x02(\x05\x12\t\n\x01q\x18\x02 \x02(\x03\x12\x0c\n\x04svar\x18\x03 \x02(\x01\x12\r\n\x05\x62ound\x18\x04 \x02(\x01\x12\x12\n\nnumSamples\x18\x05 \x02(\x05\"S\n\nDiscParams\x12\t\n\x01m\x18\x01 \x02(\x05\x12\t\n\x01q\x18\x02 \x02(\x03\x12\x0c\n\x04svar\x18\x03 \x02(\x01\x12\r\n\x05\x62ound\x18\x04 \x02(\x03\x12\x12\n\nnumSamples\x18\x05 \x02(\x05\"A\n\nRLWRParams\x12\t\n\x01m\x18\x01 \x02(\x05\x12\t\n\x01q\x18\x02 \x02(\x03\x12\t\n\x01p\x18\x03 \x02(\x03\x12\x12\n\nnumSamples\x18\x04 \x02(\x05\"\xcb\x01\n\tChallenge\x12\x13\n\x0b\x63hallengeID\x18\x01 \x02(\x05\x12\x14\n\x0cnumInstances\x18\x02 \x02(\x05\x12\x13\n\x0b\x62\x65\x61\x63onEpoch\x18\x03 \x02(\x03\x12\x14\n\x0c\x62\x65\x61\x63onOffset\x18\x04 \x02(\x05\x12\x1e\n\x07\x63params\x18\x05 \x01(\x0b\x32\x0b.ContParamsH\x00\x12\x1e\n\x07\x64params\x18\x06 \x01(\x0b\x32\x0b.DiscParamsH\x00\x12\x1e\n\x07rparams\x18\x07 \x01(\x0b\x32\x0b.RLWRParamsH\x00\x42\x08\n\x06params\"t\n\rInstanceCont1\x12\x13\n\x0b\x63hallengeID\x18\x01 \x02(\x05\x12\x12\n\ninstanceID\x18\x02 \x02(\x05\x12\x1b\n\x06params\x18\x03 \x02(\x0b\x32\x0b.ContParams\x12\x1d\n\x07samples\x18\x04 \x03(\x0b\x32\x0c.SampleCont1\"t\n\rInstanceDisc1\x12\x13\n\x0b\x63hallengeID\x18\x01 \x02(\x05\x12\x12\n\ninstanceID\x18\x02 \x02(\x05\x12\x1b\n\x06params\x18\x03 \x02(\x0b\x32\x0b.DiscParams\x12\x1d\n\x07samples\x18\x04 \x03(\x0b\x32\x0c.SampleDisc1\"t\n\rInstanceRLWR1\x12\x13\n\x0b\x63hallengeID\x18\x01 \x02(\x05\x12\x12\n\ninstanceID\x18\x02 \x02(\x05\x12\x1b\n\x06params\x18\x03 \x02(\x0b\x32\x0b.RLWRParams\x12\x1d\n\x07samples\x18\x04 \x03(\x0b\x32\x0c.SampleRLWR1\"r\n\x0cInstanceCont\x12\x13\n\x0b\x63hallengeID\x18\x01 \x02(\x05\x12\x12\n\ninstanceID\x18\x02 \x02(\x05\x12\x1b\n\x06params\x18\x03 \x02(\x0b\x32\x0b.ContParams\x12\x1c\n\x07samples\x18\x04 \x03(\x0b\x32\x0b.SampleCont\"r\n\x0cInstanceDisc\x12\x13\n\x0b\x63hallengeID\x18\x01 \x02(\x05\x12\x12\n\ninstanceID\x18\x02 \x02(\x05\x12\x1b\n\x06params\x18\x03 \x02(\x0b\x32\x0b.DiscParams\x12\x1c\n\x07samples\x18\x04 \x03(\x0b\x32\x0b.SampleDisc\"r\n\x0cInstanceRLWR\x12\x13\n\x0b\x63hallengeID\x18\x01 \x02(\x05\x12\x12\n\ninstanceID\x18\x02 \x02(\x05\x12\x1b\n\x06params\x18\x03 \x02(\x0b\x32\x0b.RLWRParams\x12\x1c\n\x07samples\x18\x04 \x03(\x0b\x32\x0b.SampleRLWR\"g\n\x07Secret1\x12\x13\n\x0b\x63hallengeID\x18\x01 \x02(\x05\x12\x12\n\ninstanceID\x18\x02 \x02(\x05\x12\t\n\x01m\x18\x03 \x02(\x05\x12\t\n\x01q\x18\x04 \x02(\x03\x12\x0c\n\x04seed\x18\x05 \x02(\x0c\x12\x0f\n\x01s\x18\x06 \x02(\x0b\x32\x04.Rq1\"l\n\x06Secret\x12\x13\n\x0b\x63hallengeID\x18\x01 \x02(\x05\x12\x12\n\ninstanceID\x18\x02 \x02(\x05\x12\t\n\x01m\x18\x03 \x02(\x05\x12\t\n\x01q\x18\x04 \x02(\x03\x12\x0c\n\x04seed\x18\x05 \x02(\x0c\x12\x15\n\x01s\x18\x06 \x02(\x0b\x32\n.RqProduct')
  ,
  dependencies=[Lol_pb2.DESCRIPTOR,RLWE_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CONTPARAMS = _descriptor.Descriptor(
  name='ContParams',
  full_name='ContParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='m', full_name='ContParams.m', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='q', full_name='ContParams.q', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svar', full_name='ContParams.svar', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bound', full_name='ContParams.bound', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numSamples', full_name='ContParams.numSamples', index=4,
      number=5, type=5, cpp_type=1, label=2,
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
  serialized_start=43,
  serialized_end=126,
)


_DISCPARAMS = _descriptor.Descriptor(
  name='DiscParams',
  full_name='DiscParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='m', full_name='DiscParams.m', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='q', full_name='DiscParams.q', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svar', full_name='DiscParams.svar', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bound', full_name='DiscParams.bound', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numSamples', full_name='DiscParams.numSamples', index=4,
      number=5, type=5, cpp_type=1, label=2,
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
  serialized_start=128,
  serialized_end=211,
)


_RLWRPARAMS = _descriptor.Descriptor(
  name='RLWRParams',
  full_name='RLWRParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='m', full_name='RLWRParams.m', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='q', full_name='RLWRParams.q', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='p', full_name='RLWRParams.p', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numSamples', full_name='RLWRParams.numSamples', index=3,
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
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=213,
  serialized_end=278,
)


_CHALLENGE = _descriptor.Descriptor(
  name='Challenge',
  full_name='Challenge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challengeID', full_name='Challenge.challengeID', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numInstances', full_name='Challenge.numInstances', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='beaconEpoch', full_name='Challenge.beaconEpoch', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='beaconOffset', full_name='Challenge.beaconOffset', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cparams', full_name='Challenge.cparams', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dparams', full_name='Challenge.dparams', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rparams', full_name='Challenge.rparams', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='params', full_name='Challenge.params',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=281,
  serialized_end=484,
)


_INSTANCECONT1 = _descriptor.Descriptor(
  name='InstanceCont1',
  full_name='InstanceCont1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challengeID', full_name='InstanceCont1.challengeID', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instanceID', full_name='InstanceCont1.instanceID', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='params', full_name='InstanceCont1.params', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='samples', full_name='InstanceCont1.samples', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=486,
  serialized_end=602,
)


_INSTANCEDISC1 = _descriptor.Descriptor(
  name='InstanceDisc1',
  full_name='InstanceDisc1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challengeID', full_name='InstanceDisc1.challengeID', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instanceID', full_name='InstanceDisc1.instanceID', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='params', full_name='InstanceDisc1.params', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='samples', full_name='InstanceDisc1.samples', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=604,
  serialized_end=720,
)


_INSTANCERLWR1 = _descriptor.Descriptor(
  name='InstanceRLWR1',
  full_name='InstanceRLWR1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challengeID', full_name='InstanceRLWR1.challengeID', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instanceID', full_name='InstanceRLWR1.instanceID', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='params', full_name='InstanceRLWR1.params', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='samples', full_name='InstanceRLWR1.samples', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=722,
  serialized_end=838,
)


_INSTANCECONT = _descriptor.Descriptor(
  name='InstanceCont',
  full_name='InstanceCont',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challengeID', full_name='InstanceCont.challengeID', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instanceID', full_name='InstanceCont.instanceID', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='params', full_name='InstanceCont.params', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='samples', full_name='InstanceCont.samples', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=840,
  serialized_end=954,
)


_INSTANCEDISC = _descriptor.Descriptor(
  name='InstanceDisc',
  full_name='InstanceDisc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challengeID', full_name='InstanceDisc.challengeID', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instanceID', full_name='InstanceDisc.instanceID', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='params', full_name='InstanceDisc.params', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='samples', full_name='InstanceDisc.samples', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=956,
  serialized_end=1070,
)


_INSTANCERLWR = _descriptor.Descriptor(
  name='InstanceRLWR',
  full_name='InstanceRLWR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challengeID', full_name='InstanceRLWR.challengeID', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instanceID', full_name='InstanceRLWR.instanceID', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='params', full_name='InstanceRLWR.params', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='samples', full_name='InstanceRLWR.samples', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1072,
  serialized_end=1186,
)


_SECRET1 = _descriptor.Descriptor(
  name='Secret1',
  full_name='Secret1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challengeID', full_name='Secret1.challengeID', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instanceID', full_name='Secret1.instanceID', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='m', full_name='Secret1.m', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='q', full_name='Secret1.q', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seed', full_name='Secret1.seed', index=4,
      number=5, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='s', full_name='Secret1.s', index=5,
      number=6, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=1188,
  serialized_end=1291,
)


_SECRET = _descriptor.Descriptor(
  name='Secret',
  full_name='Secret',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challengeID', full_name='Secret.challengeID', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instanceID', full_name='Secret.instanceID', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='m', full_name='Secret.m', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='q', full_name='Secret.q', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seed', full_name='Secret.seed', index=4,
      number=5, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='s', full_name='Secret.s', index=5,
      number=6, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=1293,
  serialized_end=1401,
)

_CHALLENGE.fields_by_name['cparams'].message_type = _CONTPARAMS
_CHALLENGE.fields_by_name['dparams'].message_type = _DISCPARAMS
_CHALLENGE.fields_by_name['rparams'].message_type = _RLWRPARAMS
_CHALLENGE.oneofs_by_name['params'].fields.append(
  _CHALLENGE.fields_by_name['cparams'])
_CHALLENGE.fields_by_name['cparams'].containing_oneof = _CHALLENGE.oneofs_by_name['params']
_CHALLENGE.oneofs_by_name['params'].fields.append(
  _CHALLENGE.fields_by_name['dparams'])
_CHALLENGE.fields_by_name['dparams'].containing_oneof = _CHALLENGE.oneofs_by_name['params']
_CHALLENGE.oneofs_by_name['params'].fields.append(
  _CHALLENGE.fields_by_name['rparams'])
_CHALLENGE.fields_by_name['rparams'].containing_oneof = _CHALLENGE.oneofs_by_name['params']
_INSTANCECONT1.fields_by_name['params'].message_type = _CONTPARAMS
_INSTANCECONT1.fields_by_name['samples'].message_type = RLWE_pb2._SAMPLECONT1
_INSTANCEDISC1.fields_by_name['params'].message_type = _DISCPARAMS
_INSTANCEDISC1.fields_by_name['samples'].message_type = RLWE_pb2._SAMPLEDISC1
_INSTANCERLWR1.fields_by_name['params'].message_type = _RLWRPARAMS
_INSTANCERLWR1.fields_by_name['samples'].message_type = RLWE_pb2._SAMPLERLWR1
_INSTANCECONT.fields_by_name['params'].message_type = _CONTPARAMS
_INSTANCECONT.fields_by_name['samples'].message_type = RLWE_pb2._SAMPLECONT
_INSTANCEDISC.fields_by_name['params'].message_type = _DISCPARAMS
_INSTANCEDISC.fields_by_name['samples'].message_type = RLWE_pb2._SAMPLEDISC
_INSTANCERLWR.fields_by_name['params'].message_type = _RLWRPARAMS
_INSTANCERLWR.fields_by_name['samples'].message_type = RLWE_pb2._SAMPLERLWR
_SECRET1.fields_by_name['s'].message_type = Lol_pb2._RQ1
_SECRET.fields_by_name['s'].message_type = Lol_pb2._RQPRODUCT
DESCRIPTOR.message_types_by_name['ContParams'] = _CONTPARAMS
DESCRIPTOR.message_types_by_name['DiscParams'] = _DISCPARAMS
DESCRIPTOR.message_types_by_name['RLWRParams'] = _RLWRPARAMS
DESCRIPTOR.message_types_by_name['Challenge'] = _CHALLENGE
DESCRIPTOR.message_types_by_name['InstanceCont1'] = _INSTANCECONT1
DESCRIPTOR.message_types_by_name['InstanceDisc1'] = _INSTANCEDISC1
DESCRIPTOR.message_types_by_name['InstanceRLWR1'] = _INSTANCERLWR1
DESCRIPTOR.message_types_by_name['InstanceCont'] = _INSTANCECONT
DESCRIPTOR.message_types_by_name['InstanceDisc'] = _INSTANCEDISC
DESCRIPTOR.message_types_by_name['InstanceRLWR'] = _INSTANCERLWR
DESCRIPTOR.message_types_by_name['Secret1'] = _SECRET1
DESCRIPTOR.message_types_by_name['Secret'] = _SECRET

ContParams = _reflection.GeneratedProtocolMessageType('ContParams', (_message.Message,), dict(
  DESCRIPTOR = _CONTPARAMS,
  __module__ = 'Challenges_pb2'
  # @@protoc_insertion_point(class_scope:ContParams)
  ))
_sym_db.RegisterMessage(ContParams)

DiscParams = _reflection.GeneratedProtocolMessageType('DiscParams', (_message.Message,), dict(
  DESCRIPTOR = _DISCPARAMS,
  __module__ = 'Challenges_pb2'
  # @@protoc_insertion_point(class_scope:DiscParams)
  ))
_sym_db.RegisterMessage(DiscParams)

RLWRParams = _reflection.GeneratedProtocolMessageType('RLWRParams', (_message.Message,), dict(
  DESCRIPTOR = _RLWRPARAMS,
  __module__ = 'Challenges_pb2'
  # @@protoc_insertion_point(class_scope:RLWRParams)
  ))
_sym_db.RegisterMessage(RLWRParams)

Challenge = _reflection.GeneratedProtocolMessageType('Challenge', (_message.Message,), dict(
  DESCRIPTOR = _CHALLENGE,
  __module__ = 'Challenges_pb2'
  # @@protoc_insertion_point(class_scope:Challenge)
  ))
_sym_db.RegisterMessage(Challenge)

InstanceCont1 = _reflection.GeneratedProtocolMessageType('InstanceCont1', (_message.Message,), dict(
  DESCRIPTOR = _INSTANCECONT1,
  __module__ = 'Challenges_pb2'
  # @@protoc_insertion_point(class_scope:InstanceCont1)
  ))
_sym_db.RegisterMessage(InstanceCont1)

InstanceDisc1 = _reflection.GeneratedProtocolMessageType('InstanceDisc1', (_message.Message,), dict(
  DESCRIPTOR = _INSTANCEDISC1,
  __module__ = 'Challenges_pb2'
  # @@protoc_insertion_point(class_scope:InstanceDisc1)
  ))
_sym_db.RegisterMessage(InstanceDisc1)

InstanceRLWR1 = _reflection.GeneratedProtocolMessageType('InstanceRLWR1', (_message.Message,), dict(
  DESCRIPTOR = _INSTANCERLWR1,
  __module__ = 'Challenges_pb2'
  # @@protoc_insertion_point(class_scope:InstanceRLWR1)
  ))
_sym_db.RegisterMessage(InstanceRLWR1)

InstanceCont = _reflection.GeneratedProtocolMessageType('InstanceCont', (_message.Message,), dict(
  DESCRIPTOR = _INSTANCECONT,
  __module__ = 'Challenges_pb2'
  # @@protoc_insertion_point(class_scope:InstanceCont)
  ))
_sym_db.RegisterMessage(InstanceCont)

InstanceDisc = _reflection.GeneratedProtocolMessageType('InstanceDisc', (_message.Message,), dict(
  DESCRIPTOR = _INSTANCEDISC,
  __module__ = 'Challenges_pb2'
  # @@protoc_insertion_point(class_scope:InstanceDisc)
  ))
_sym_db.RegisterMessage(InstanceDisc)

InstanceRLWR = _reflection.GeneratedProtocolMessageType('InstanceRLWR', (_message.Message,), dict(
  DESCRIPTOR = _INSTANCERLWR,
  __module__ = 'Challenges_pb2'
  # @@protoc_insertion_point(class_scope:InstanceRLWR)
  ))
_sym_db.RegisterMessage(InstanceRLWR)

Secret1 = _reflection.GeneratedProtocolMessageType('Secret1', (_message.Message,), dict(
  DESCRIPTOR = _SECRET1,
  __module__ = 'Challenges_pb2'
  # @@protoc_insertion_point(class_scope:Secret1)
  ))
_sym_db.RegisterMessage(Secret1)

Secret = _reflection.GeneratedProtocolMessageType('Secret', (_message.Message,), dict(
  DESCRIPTOR = _SECRET,
  __module__ = 'Challenges_pb2'
  # @@protoc_insertion_point(class_scope:Secret)
  ))
_sym_db.RegisterMessage(Secret)


# @@protoc_insertion_point(module_scope)
