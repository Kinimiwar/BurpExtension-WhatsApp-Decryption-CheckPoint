# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: whatsapp.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='whatsapp.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0ewhatsapp.proto\"\xb7\x03\n\x0eWebMessageInfo\x12\x18\n\x03key\x18\x01 \x01(\x0b\x32\x0b.MessageKey\x12\x19\n\x07message\x18\x02 \x01(\x0b\x32\x08.Message\x12\x18\n\x10messageTimestamp\x18\x03 \x01(\x04\x12\x17\n\x06status\x18\x04 \x01(\x0e\x32\x07.STATUS\x12\x13\n\x0bparticipant\x18\x05 \x01(\t\x12\x0e\n\x06ignore\x18\x06 \x01(\x08\x12\x0f\n\x07starred\x18\x07 \x01(\x08\x12\x11\n\tbroadcast\x18\x08 \x01(\x08\x12\x10\n\x08pushName\x18\t \x01(\t\x12\x1d\n\x15mediaCiphertextSha256\x18\n \x01(\t\x12\x11\n\tmulticast\x18\x0b \x01(\x08\x12\x0f\n\x07urlText\x18\x0c \x01(\x08\x12\x11\n\turlNumber\x18\r \x01(\x08\x12\"\n\x0fmessageStubType\x18\x0e \x01(\x0e\x32\t.STUBTYPE\x12\x12\n\nclearMedia\x18\x0f \x01(\x08\x12\x1d\n\x15messageStubParameters\x18\x10 \x01(\t\x12\x10\n\x08\x64uration\x18\x11 \x01(\r\x12\x0e\n\x06labels\x18\x12 \x01(\t\x12\x13\n\x0bpaymentInfo\x18\x13 \x01(\x0c\"P\n\nMessageKey\x12\x11\n\tremoteJid\x18\x01 \x01(\t\x12\x0e\n\x06\x66romMe\x18\x02 \x01(\x08\x12\n\n\x02id\x18\x03 \x01(\t\x12\x13\n\x0bparticipant\x18\x04 \x01(\t\"\x1f\n\x07Message\x12\x14\n\x0c\x63onversation\x18\x01 \x01(\t*X\n\x06STATUS\x12\t\n\x05\x45RROR\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0e\n\nSERVER_ACK\x10\x02\x12\x10\n\x0c\x44\x45LIVERY_ACK\x10\x03\x12\x08\n\x04READ\x10\x04\x12\n\n\x06PLAYED\x10\x05*\xd6\r\n\x08STUBTYPE\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06REVOKE\x10\x01\x12\x0e\n\nCIPHERTEXT\x10\x02\x12\x0f\n\x0b\x46UTUREPROOF\x10\x04\x12\x1b\n\x17NON_VERIFIED_TRANSITION\x10\x05\x12\x19\n\x15UNVERIFIED_TRANSITION\x10\x06\x12\x17\n\x13VERIFIED_TRANSITION\x10\x07\x12\x18\n\x14VERIFIED_LOW_UNKNOWN\x10\x08\x12\x11\n\rVERIFIED_HIGH\x10\t\x12\x1c\n\x18VERIFIED_INITIAL_UNKNOWN\x10\n\x12\x18\n\x14VERIFIED_INITIAL_LOW\x10\x0b\x12\x19\n\x15VERIFIED_INITIAL_HIGH\x10\x0c\x12#\n\x1fVERIFIED_TRANSITION_ANY_TO_NONE\x10\r\x12#\n\x1fVERIFIED_TRANSITION_ANY_TO_HIGH\x10\x0e\x12#\n\x1fVERIFIED_TRANSITION_HIGH_TO_LOW\x10\x0f\x12\'\n#VERIFIED_TRANSITION_HIGH_TO_UNKNOWN\x10\x10\x12&\n\"VERIFIED_TRANSITION_UNKNOWN_TO_LOW\x10\x11\x12&\n\"VERIFIED_TRANSITION_LOW_TO_UNKNOWN\x10\x12\x12#\n\x1fVERIFIED_TRANSITION_NONE_TO_LOW\x10\x13\x12\'\n#VERIFIED_TRANSITION_NONE_TO_UNKNOWN\x10\x14\x12\x10\n\x0cGROUP_CREATE\x10\x15\x12\x18\n\x14GROUP_CHANGE_SUBJECT\x10\x16\x12\x15\n\x11GROUP_CHANGE_ICON\x10\x17\x12\x1c\n\x18GROUP_CHANGE_INVITE_LINK\x10\x18\x12\x1c\n\x18GROUP_CHANGE_DESCRIPTION\x10\x19\x12\x19\n\x15GROUP_CHANGE_RESTRICT\x10\x1a\x12\x19\n\x15GROUP_CHANGE_ANNOUNCE\x10\x1b\x12\x19\n\x15GROUP_PARTICIPANT_ADD\x10\x1c\x12\x1c\n\x18GROUP_PARTICIPANT_REMOVE\x10\x1d\x12\x1d\n\x19GROUP_PARTICIPANT_PROMOTE\x10\x1e\x12\x1c\n\x18GROUP_PARTICIPANT_DEMOTE\x10\x1f\x12\x1c\n\x18GROUP_PARTICIPANT_INVITE\x10 \x12\x1b\n\x17GROUP_PARTICIPANT_LEAVE\x10!\x12#\n\x1fGROUP_PARTICIPANT_CHANGE_NUMBER\x10\"\x12\x14\n\x10\x42ROADCAST_CREATE\x10#\x12\x11\n\rBROADCAST_ADD\x10$\x12\x14\n\x10\x42ROADCAST_REMOVE\x10%\x12\x18\n\x14GENERIC_NOTIFICATION\x10&\x12\x18\n\x14\x45\x32\x45_IDENTITY_CHANGED\x10\'\x12\x11\n\rE2E_ENCRYPTED\x10(\x12\x15\n\x11\x43\x41LL_MISSED_VOICE\x10)\x12\x15\n\x11\x43\x41LL_MISSED_VIDEO\x10*\x12\x1c\n\x18INDIVIDUAL_CHANGE_NUMBER\x10+\x12\x10\n\x0cGROUP_DELETE\x10,\x12&\n\"GROUP_ANNOUNCE_MODE_MESSAGE_BOUNCE\x10-\x12\x1b\n\x17\x43\x41LL_MISSED_GROUP_VOICE\x10.\x12\x1b\n\x17\x43\x41LL_MISSED_GROUP_VIDEO\x10/\x12\x16\n\x12PAYMENT_CIPHERTEXT\x10\x30\x12\x17\n\x13PAYMENT_FUTUREPROOF\x10\x31\x12,\n(PAYMENT_TRANSACTION_STATUS_UPDATE_FAILED\x10\x32\x12.\n*PAYMENT_TRANSACTION_STATUS_UPDATE_REFUNDED\x10\x33\x12\x33\n/PAYMENT_TRANSACTION_STATUS_UPDATE_REFUND_FAILED\x10\x34\x12\x35\n1PAYMENT_TRANSACTION_STATUS_RECEIVER_PENDING_SETUP\x10\x35\x12<\n8PAYMENT_TRANSACTION_STATUS_RECEIVER_SUCCESS_AFTER_HICCUP\x10\x36\x12)\n%PAYMENT_ACTION_ACCOUNT_SETUP_REMINDER\x10\x37\x12(\n$PAYMENT_ACTION_SEND_PAYMENT_REMINDER\x10\x38\x12*\n&PAYMENT_ACTION_SEND_PAYMENT_INVITATION\x10\x39')
)

_STATUS = _descriptor.EnumDescriptor(
  name='STATUS',
  full_name='STATUS',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVER_ACK', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELIVERY_ACK', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYED', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=575,
  serialized_end=663,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

STATUS = enum_type_wrapper.EnumTypeWrapper(_STATUS)
_STUBTYPE = _descriptor.EnumDescriptor(
  name='STUBTYPE',
  full_name='STUBTYPE',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REVOKE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CIPHERTEXT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FUTUREPROOF', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NON_VERIFIED_TRANSITION', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNVERIFIED_TRANSITION', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERIFIED_TRANSITION', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERIFIED_LOW_UNKNOWN', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERIFIED_HIGH', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERIFIED_INITIAL_UNKNOWN', index=9, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERIFIED_INITIAL_LOW', index=10, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERIFIED_INITIAL_HIGH', index=11, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERIFIED_TRANSITION_ANY_TO_NONE', index=12, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERIFIED_TRANSITION_ANY_TO_HIGH', index=13, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERIFIED_TRANSITION_HIGH_TO_LOW', index=14, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERIFIED_TRANSITION_HIGH_TO_UNKNOWN', index=15, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERIFIED_TRANSITION_UNKNOWN_TO_LOW', index=16, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERIFIED_TRANSITION_LOW_TO_UNKNOWN', index=17, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERIFIED_TRANSITION_NONE_TO_LOW', index=18, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERIFIED_TRANSITION_NONE_TO_UNKNOWN', index=19, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP_CREATE', index=20, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP_CHANGE_SUBJECT', index=21, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP_CHANGE_ICON', index=22, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP_CHANGE_INVITE_LINK', index=23, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP_CHANGE_DESCRIPTION', index=24, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP_CHANGE_RESTRICT', index=25, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP_CHANGE_ANNOUNCE', index=26, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP_PARTICIPANT_ADD', index=27, number=28,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP_PARTICIPANT_REMOVE', index=28, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP_PARTICIPANT_PROMOTE', index=29, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP_PARTICIPANT_DEMOTE', index=30, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP_PARTICIPANT_INVITE', index=31, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP_PARTICIPANT_LEAVE', index=32, number=33,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP_PARTICIPANT_CHANGE_NUMBER', index=33, number=34,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BROADCAST_CREATE', index=34, number=35,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BROADCAST_ADD', index=35, number=36,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BROADCAST_REMOVE', index=36, number=37,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GENERIC_NOTIFICATION', index=37, number=38,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E2E_IDENTITY_CHANGED', index=38, number=39,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E2E_ENCRYPTED', index=39, number=40,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALL_MISSED_VOICE', index=40, number=41,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALL_MISSED_VIDEO', index=41, number=42,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDIVIDUAL_CHANGE_NUMBER', index=42, number=43,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP_DELETE', index=43, number=44,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP_ANNOUNCE_MODE_MESSAGE_BOUNCE', index=44, number=45,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALL_MISSED_GROUP_VOICE', index=45, number=46,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALL_MISSED_GROUP_VIDEO', index=46, number=47,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAYMENT_CIPHERTEXT', index=47, number=48,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAYMENT_FUTUREPROOF', index=48, number=49,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAYMENT_TRANSACTION_STATUS_UPDATE_FAILED', index=49, number=50,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAYMENT_TRANSACTION_STATUS_UPDATE_REFUNDED', index=50, number=51,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAYMENT_TRANSACTION_STATUS_UPDATE_REFUND_FAILED', index=51, number=52,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAYMENT_TRANSACTION_STATUS_RECEIVER_PENDING_SETUP', index=52, number=53,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAYMENT_TRANSACTION_STATUS_RECEIVER_SUCCESS_AFTER_HICCUP', index=53, number=54,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAYMENT_ACTION_ACCOUNT_SETUP_REMINDER', index=54, number=55,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAYMENT_ACTION_SEND_PAYMENT_REMINDER', index=55, number=56,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAYMENT_ACTION_SEND_PAYMENT_INVITATION', index=56, number=57,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=666,
  serialized_end=2416,
)
_sym_db.RegisterEnumDescriptor(_STUBTYPE)

STUBTYPE = enum_type_wrapper.EnumTypeWrapper(_STUBTYPE)
ERROR = 0
PENDING = 1
SERVER_ACK = 2
DELIVERY_ACK = 3
READ = 4
PLAYED = 5
UNKNOWN = 0
REVOKE = 1
CIPHERTEXT = 2
FUTUREPROOF = 4
NON_VERIFIED_TRANSITION = 5
UNVERIFIED_TRANSITION = 6
VERIFIED_TRANSITION = 7
VERIFIED_LOW_UNKNOWN = 8
VERIFIED_HIGH = 9
VERIFIED_INITIAL_UNKNOWN = 10
VERIFIED_INITIAL_LOW = 11
VERIFIED_INITIAL_HIGH = 12
VERIFIED_TRANSITION_ANY_TO_NONE = 13
VERIFIED_TRANSITION_ANY_TO_HIGH = 14
VERIFIED_TRANSITION_HIGH_TO_LOW = 15
VERIFIED_TRANSITION_HIGH_TO_UNKNOWN = 16
VERIFIED_TRANSITION_UNKNOWN_TO_LOW = 17
VERIFIED_TRANSITION_LOW_TO_UNKNOWN = 18
VERIFIED_TRANSITION_NONE_TO_LOW = 19
VERIFIED_TRANSITION_NONE_TO_UNKNOWN = 20
GROUP_CREATE = 21
GROUP_CHANGE_SUBJECT = 22
GROUP_CHANGE_ICON = 23
GROUP_CHANGE_INVITE_LINK = 24
GROUP_CHANGE_DESCRIPTION = 25
GROUP_CHANGE_RESTRICT = 26
GROUP_CHANGE_ANNOUNCE = 27
GROUP_PARTICIPANT_ADD = 28
GROUP_PARTICIPANT_REMOVE = 29
GROUP_PARTICIPANT_PROMOTE = 30
GROUP_PARTICIPANT_DEMOTE = 31
GROUP_PARTICIPANT_INVITE = 32
GROUP_PARTICIPANT_LEAVE = 33
GROUP_PARTICIPANT_CHANGE_NUMBER = 34
BROADCAST_CREATE = 35
BROADCAST_ADD = 36
BROADCAST_REMOVE = 37
GENERIC_NOTIFICATION = 38
E2E_IDENTITY_CHANGED = 39
E2E_ENCRYPTED = 40
CALL_MISSED_VOICE = 41
CALL_MISSED_VIDEO = 42
INDIVIDUAL_CHANGE_NUMBER = 43
GROUP_DELETE = 44
GROUP_ANNOUNCE_MODE_MESSAGE_BOUNCE = 45
CALL_MISSED_GROUP_VOICE = 46
CALL_MISSED_GROUP_VIDEO = 47
PAYMENT_CIPHERTEXT = 48
PAYMENT_FUTUREPROOF = 49
PAYMENT_TRANSACTION_STATUS_UPDATE_FAILED = 50
PAYMENT_TRANSACTION_STATUS_UPDATE_REFUNDED = 51
PAYMENT_TRANSACTION_STATUS_UPDATE_REFUND_FAILED = 52
PAYMENT_TRANSACTION_STATUS_RECEIVER_PENDING_SETUP = 53
PAYMENT_TRANSACTION_STATUS_RECEIVER_SUCCESS_AFTER_HICCUP = 54
PAYMENT_ACTION_ACCOUNT_SETUP_REMINDER = 55
PAYMENT_ACTION_SEND_PAYMENT_REMINDER = 56
PAYMENT_ACTION_SEND_PAYMENT_INVITATION = 57



_WEBMESSAGEINFO = _descriptor.Descriptor(
  name='WebMessageInfo',
  full_name='WebMessageInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='WebMessageInfo.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='WebMessageInfo.message', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='messageTimestamp', full_name='WebMessageInfo.messageTimestamp', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='WebMessageInfo.status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='participant', full_name='WebMessageInfo.participant', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ignore', full_name='WebMessageInfo.ignore', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='starred', full_name='WebMessageInfo.starred', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='broadcast', full_name='WebMessageInfo.broadcast', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pushName', full_name='WebMessageInfo.pushName', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mediaCiphertextSha256', full_name='WebMessageInfo.mediaCiphertextSha256', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multicast', full_name='WebMessageInfo.multicast', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='urlText', full_name='WebMessageInfo.urlText', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='urlNumber', full_name='WebMessageInfo.urlNumber', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='messageStubType', full_name='WebMessageInfo.messageStubType', index=13,
      number=14, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clearMedia', full_name='WebMessageInfo.clearMedia', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='messageStubParameters', full_name='WebMessageInfo.messageStubParameters', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='WebMessageInfo.duration', index=16,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='WebMessageInfo.labels', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paymentInfo', full_name='WebMessageInfo.paymentInfo', index=18,
      number=19, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=19,
  serialized_end=458,
)


_MESSAGEKEY = _descriptor.Descriptor(
  name='MessageKey',
  full_name='MessageKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='remoteJid', full_name='MessageKey.remoteJid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fromMe', full_name='MessageKey.fromMe', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='MessageKey.id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='participant', full_name='MessageKey.participant', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=460,
  serialized_end=540,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conversation', full_name='Message.conversation', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=542,
  serialized_end=573,
)

_WEBMESSAGEINFO.fields_by_name['key'].message_type = _MESSAGEKEY
_WEBMESSAGEINFO.fields_by_name['message'].message_type = _MESSAGE
_WEBMESSAGEINFO.fields_by_name['status'].enum_type = _STATUS
_WEBMESSAGEINFO.fields_by_name['messageStubType'].enum_type = _STUBTYPE
DESCRIPTOR.message_types_by_name['WebMessageInfo'] = _WEBMESSAGEINFO
DESCRIPTOR.message_types_by_name['MessageKey'] = _MESSAGEKEY
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.enum_types_by_name['STATUS'] = _STATUS
DESCRIPTOR.enum_types_by_name['STUBTYPE'] = _STUBTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WebMessageInfo = _reflection.GeneratedProtocolMessageType('WebMessageInfo', (_message.Message,), dict(
  DESCRIPTOR = _WEBMESSAGEINFO,
  __module__ = 'whatsapp_pb2'
  # @@protoc_insertion_point(class_scope:WebMessageInfo)
  ))
_sym_db.RegisterMessage(WebMessageInfo)

MessageKey = _reflection.GeneratedProtocolMessageType('MessageKey', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGEKEY,
  __module__ = 'whatsapp_pb2'
  # @@protoc_insertion_point(class_scope:MessageKey)
  ))
_sym_db.RegisterMessage(MessageKey)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'whatsapp_pb2'
  # @@protoc_insertion_point(class_scope:Message)
  ))
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)
