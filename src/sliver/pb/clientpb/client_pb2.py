# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: clientpb/client.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..commonpb import common_pb2 as commonpb_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x63lientpb/client.proto\x12\x08\x63lientpb\x1a\x15\x63ommonpb/common.proto\"\x83\x01\n\x07Version\x12\r\n\x05Major\x18\x01 \x01(\x05\x12\r\n\x05Minor\x18\x02 \x01(\x05\x12\r\n\x05Patch\x18\x03 \x01(\x05\x12\x0e\n\x06\x43ommit\x18\x04 \x01(\t\x12\r\n\x05\x44irty\x18\x05 \x01(\x08\x12\x12\n\nCompiledAt\x18\x06 \x01(\x03\x12\n\n\x02OS\x18\x07 \x01(\t\x12\x0c\n\x04\x41rch\x18\x08 \x01(\t\"\xb2\x03\n\x07Session\x12\n\n\x02ID\x18\x01 \x01(\t\x12\x0c\n\x04Name\x18\x02 \x01(\t\x12\x10\n\x08Hostname\x18\x03 \x01(\t\x12\x0c\n\x04UUID\x18\x04 \x01(\t\x12\x10\n\x08Username\x18\x05 \x01(\t\x12\x0b\n\x03UID\x18\x06 \x01(\t\x12\x0b\n\x03GID\x18\x07 \x01(\t\x12\n\n\x02OS\x18\x08 \x01(\t\x12\x0c\n\x04\x41rch\x18\t \x01(\t\x12\x11\n\tTransport\x18\n \x01(\t\x12\x15\n\rRemoteAddress\x18\x0b \x01(\t\x12\x0b\n\x03PID\x18\x0c \x01(\x05\x12\x10\n\x08\x46ilename\x18\r \x01(\t\x12\x13\n\x0bLastCheckin\x18\x0e \x01(\x03\x12\x10\n\x08\x41\x63tiveC2\x18\x0f \x01(\t\x12\x0f\n\x07Version\x18\x10 \x01(\t\x12\x0f\n\x07\x45vasion\x18\x11 \x01(\x08\x12\x0e\n\x06IsDead\x18\x12 \x01(\x08\x12\x19\n\x11ReconnectInterval\x18\x13 \x01(\x03\x12\x10\n\x08ProxyURL\x18\x14 \x01(\t\x12\x0e\n\x06\x42urned\x18\x16 \x01(\x08\x12\x12\n\nExtensions\x18\x17 \x03(\t\x12\x0e\n\x06PeerID\x18\x19 \x01(\x03\x12\x0e\n\x06Locale\x18\x1a \x01(\t\x12\x14\n\x0c\x46irstContact\x18\x1b \x01(\x03\"\xf5\x03\n\x06\x42\x65\x61\x63on\x12\n\n\x02ID\x18\x01 \x01(\t\x12\x0c\n\x04Name\x18\x02 \x01(\t\x12\x10\n\x08Hostname\x18\x03 \x01(\t\x12\x0c\n\x04UUID\x18\x04 \x01(\t\x12\x10\n\x08Username\x18\x05 \x01(\t\x12\x0b\n\x03UID\x18\x06 \x01(\t\x12\x0b\n\x03GID\x18\x07 \x01(\t\x12\n\n\x02OS\x18\x08 \x01(\t\x12\x0c\n\x04\x41rch\x18\t \x01(\t\x12\x11\n\tTransport\x18\n \x01(\t\x12\x15\n\rRemoteAddress\x18\x0b \x01(\t\x12\x0b\n\x03PID\x18\x0c \x01(\x05\x12\x10\n\x08\x46ilename\x18\r \x01(\t\x12\x13\n\x0bLastCheckin\x18\x0e \x01(\x03\x12\x10\n\x08\x41\x63tiveC2\x18\x0f \x01(\t\x12\x0f\n\x07Version\x18\x10 \x01(\t\x12\x0f\n\x07\x45vasion\x18\x11 \x01(\x08\x12\x0e\n\x06IsDead\x18\x12 \x01(\x08\x12\x10\n\x08ProxyURL\x18\x14 \x01(\t\x12\x19\n\x11ReconnectInterval\x18\x15 \x01(\x03\x12\x10\n\x08Interval\x18\x16 \x01(\x03\x12\x0e\n\x06Jitter\x18\x17 \x01(\x03\x12\x0e\n\x06\x42urned\x18\x18 \x01(\x08\x12\x13\n\x0bNextCheckin\x18\x19 \x01(\x03\x12\x12\n\nTasksCount\x18\x1a \x01(\x03\x12\x1b\n\x13TasksCountCompleted\x18\x1b \x01(\x03\x12\x0e\n\x06Locale\x18\x1c \x01(\t\x12\x14\n\x0c\x46irstContact\x18\x1d \x01(\x03\",\n\x07\x42\x65\x61\x63ons\x12!\n\x07\x42\x65\x61\x63ons\x18\x02 \x03(\x0b\x32\x10.clientpb.Beacon\"\xa9\x01\n\nBeaconTask\x12\n\n\x02ID\x18\x01 \x01(\t\x12\x10\n\x08\x42\x65\x61\x63onID\x18\x02 \x01(\t\x12\x11\n\tCreatedAt\x18\x03 \x01(\x03\x12\r\n\x05State\x18\x04 \x01(\t\x12\x0e\n\x06SentAt\x18\x05 \x01(\x03\x12\x13\n\x0b\x43ompletedAt\x18\x06 \x01(\x03\x12\x0f\n\x07Request\x18\x07 \x01(\x0c\x12\x10\n\x08Response\x18\x08 \x01(\x0c\x12\x13\n\x0b\x44\x65scription\x18\t \x01(\t\"D\n\x0b\x42\x65\x61\x63onTasks\x12\x10\n\x08\x42\x65\x61\x63onID\x18\x01 \x01(\t\x12#\n\x05Tasks\x18\x02 \x03(\x0b\x32\x14.clientpb.BeaconTask\";\n\tImplantC2\x12\x10\n\x08Priority\x18\x01 \x01(\r\x12\x0b\n\x03URL\x18\x02 \x01(\t\x12\x0f\n\x07Options\x18\x03 \x01(\t\"\x98\x07\n\rImplantConfig\x12\n\n\x02ID\x18\x01 \x01(\t\x12\x10\n\x08IsBeacon\x18\x02 \x01(\x08\x12\x16\n\x0e\x42\x65\x61\x63onInterval\x18\x03 \x01(\x03\x12\x14\n\x0c\x42\x65\x61\x63onJitter\x18\x04 \x01(\x03\x12\x0c\n\x04GOOS\x18\x05 \x01(\t\x12\x0e\n\x06GOARCH\x18\x06 \x01(\t\x12\x0c\n\x04Name\x18\x07 \x01(\t\x12\r\n\x05\x44\x65\x62ug\x18\x08 \x01(\x08\x12\x0f\n\x07\x45vasion\x18\t \x01(\x08\x12\x18\n\x10ObfuscateSymbols\x18\n \x01(\x08\x12\x12\n\nMtlsCACert\x18\x14 \x01(\t\x12\x10\n\x08MtlsCert\x18\x15 \x01(\t\x12\x0f\n\x07MtlsKey\x18\x16 \x01(\t\x12\x14\n\x0c\x45\x43\x43PublicKey\x18\x17 \x01(\t\x12\x15\n\rECCPrivateKey\x18\x18 \x01(\t\x12\x1d\n\x15\x45\x43\x43PublicKeySignature\x18\x19 \x01(\t\x12\x1f\n\x17MinisignServerPublicKey\x18\x1a \x01(\t\x12\x18\n\x10WGImplantPrivKey\x18\x1e \x01(\t\x12\x16\n\x0eWGServerPubKey\x18\x1f \x01(\t\x12\x13\n\x0bWGPeerTunIP\x18  \x01(\t\x12\x19\n\x11WGKeyExchangePort\x18! \x01(\r\x12\x16\n\x0eWGTcpCommsPort\x18\" \x01(\r\x12\x19\n\x11ReconnectInterval\x18( \x01(\x03\x12\x1b\n\x13MaxConnectionErrors\x18) \x01(\r\x12\x13\n\x0bPollTimeout\x18* \x01(\x03\x12\x1f\n\x02\x43\x32\x18\x32 \x03(\x0b\x32\x13.clientpb.ImplantC2\x12\x15\n\rCanaryDomains\x18\x33 \x03(\t\x12\x1a\n\x12\x43onnectionStrategy\x18\x34 \x01(\t\x12\x19\n\x11LimitDomainJoined\x18< \x01(\x08\x12\x15\n\rLimitDatetime\x18= \x01(\t\x12\x15\n\rLimitHostname\x18> \x01(\t\x12\x15\n\rLimitUsername\x18? \x01(\t\x12\x17\n\x0fLimitFileExists\x18@ \x01(\t\x12\x13\n\x0bLimitLocale\x18\x41 \x01(\t\x12&\n\x06\x46ormat\x18\x64 \x01(\x0e\x32\x16.clientpb.OutputFormat\x12\x13\n\x0bIsSharedLib\x18\x65 \x01(\x08\x12\x10\n\x08\x46ileName\x18\x66 \x01(\t\x12\x11\n\tIsService\x18g \x01(\x08\x12\x13\n\x0bIsShellcode\x18h \x01(\x08\x12\x11\n\tRunAtLoad\x18i \x01(\x08\"a\n\x15\x45xternalImplantConfig\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\'\n\x06\x43onfig\x18\x02 \x01(\x0b\x32\x17.clientpb.ImplantConfig\x12\x11\n\tOTPSecret\x18\x03 \x01(\t\"\\\n\x15\x45xternalImplantBinary\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x17\n\x0fImplantConfigID\x18\x02 \x01(\t\x12\x1c\n\x04\x46ile\x18\x03 \x01(\x0b\x32\x0e.commonpb.File\"\x8f\x01\n\rImplantBuilds\x12\x35\n\x07\x43onfigs\x18\x01 \x03(\x0b\x32$.clientpb.ImplantBuilds.ConfigsEntry\x1aG\n\x0c\x43onfigsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.clientpb.ImplantConfig:\x02\x38\x01\"V\n\x0e\x43ompilerTarget\x12\x0c\n\x04GOOS\x18\x01 \x01(\t\x12\x0e\n\x06GOARCH\x18\x02 \x01(\t\x12&\n\x06\x46ormat\x18\x03 \x01(\x0e\x32\x16.clientpb.OutputFormat\"Z\n\rCrossCompiler\x12\x12\n\nTargetGOOS\x18\x01 \x01(\t\x12\x14\n\x0cTargetGOARCH\x18\x02 \x01(\t\x12\x0e\n\x06\x43\x43Path\x18\x03 \x01(\t\x12\x0f\n\x07\x43XXPath\x18\x04 \x01(\t\"\xba\x01\n\x08\x43ompiler\x12\x0c\n\x04GOOS\x18\x01 \x01(\t\x12\x0e\n\x06GOARCH\x18\x02 \x01(\t\x12)\n\x07Targets\x18\x03 \x03(\x0b\x32\x18.clientpb.CompilerTarget\x12/\n\x0e\x43rossCompilers\x18\x04 \x03(\x0b\x32\x17.clientpb.CrossCompiler\x12\x34\n\x12UnsupportedTargets\x18\x05 \x03(\x0b\x32\x18.clientpb.CompilerTarget\"\x19\n\tDeleteReq\x12\x0c\n\x04Name\x18\x01 \x01(\t\"\x81\x01\n\tDNSCanary\x12\x13\n\x0bImplantName\x18\x01 \x01(\t\x12\x0e\n\x06\x44omain\x18\x02 \x01(\t\x12\x11\n\tTriggered\x18\x03 \x01(\x08\x12\x16\n\x0e\x46irstTriggered\x18\x04 \x01(\t\x12\x15\n\rLatestTrigger\x18\x05 \x01(\t\x12\r\n\x05\x43ount\x18\x06 \x01(\r\"1\n\x08\x43\x61naries\x12%\n\x08\x43\x61naries\x18\x01 \x03(\x0b\x32\x13.clientpb.DNSCanary\"\x18\n\nUniqueWGIP\x12\n\n\x02IP\x18\x01 \x01(\t\"G\n\x0eImplantProfile\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\'\n\x06\x43onfig\x18\x02 \x01(\x0b\x32\x17.clientpb.ImplantConfig\"=\n\x0fImplantProfiles\x12*\n\x08Profiles\x18\x01 \x03(\x0b\x32\x18.clientpb.ImplantProfile\"$\n\rRegenerateReq\x12\x13\n\x0bImplantName\x18\x01 \x01(\t\"e\n\x03Job\x12\n\n\x02ID\x18\x01 \x01(\r\x12\x0c\n\x04Name\x18\x02 \x01(\t\x12\x13\n\x0b\x44\x65scription\x18\x03 \x01(\t\x12\x10\n\x08Protocol\x18\x04 \x01(\t\x12\x0c\n\x04Port\x18\x05 \x01(\r\x12\x0f\n\x07\x44omains\x18\x06 \x03(\t\"%\n\x04Jobs\x12\x1d\n\x06\x41\x63tive\x18\x01 \x03(\x0b\x32\r.clientpb.Job\"\x18\n\nKillJobReq\x12\n\n\x02ID\x18\x01 \x01(\r\"&\n\x07KillJob\x12\n\n\x02ID\x18\x01 \x01(\r\x12\x0f\n\x07Success\x18\x02 \x01(\x08\"A\n\x0fMTLSListenerReq\x12\x0c\n\x04Host\x18\x01 \x01(\t\x12\x0c\n\x04Port\x18\x02 \x01(\r\x12\x12\n\nPersistent\x18\x03 \x01(\x08\"\x1d\n\x0cMTLSListener\x12\r\n\x05JobID\x18\x01 \x01(\r\"n\n\rWGListenerReq\x12\x0c\n\x04Host\x18\x06 \x01(\t\x12\x0c\n\x04Port\x18\x01 \x01(\r\x12\r\n\x05TunIP\x18\x02 \x01(\t\x12\r\n\x05NPort\x18\x03 \x01(\r\x12\x0f\n\x07KeyPort\x18\x04 \x01(\r\x12\x12\n\nPersistent\x18\x05 \x01(\x08\"\x1b\n\nWGListener\x12\r\n\x05JobID\x18\x01 \x01(\r\"w\n\x0e\x44NSListenerReq\x12\x0f\n\x07\x44omains\x18\x01 \x03(\t\x12\x10\n\x08\x43\x61naries\x18\x02 \x01(\x08\x12\x0c\n\x04Host\x18\x03 \x01(\t\x12\x0c\n\x04Port\x18\x04 \x01(\r\x12\x12\n\nPersistent\x18\x05 \x01(\x08\x12\x12\n\nEnforceOTP\x18\x06 \x01(\x08\"\x1c\n\x0b\x44NSListener\x12\r\n\x05JobID\x18\x01 \x01(\r\"\xf7\x01\n\x0fHTTPListenerReq\x12\x0e\n\x06\x44omain\x18\x01 \x01(\t\x12\x0c\n\x04Host\x18\x02 \x01(\t\x12\x0c\n\x04Port\x18\x03 \x01(\r\x12\x0e\n\x06Secure\x18\x04 \x01(\x08\x12\x0f\n\x07Website\x18\x05 \x01(\t\x12\x0c\n\x04\x43\x65rt\x18\x06 \x01(\x0c\x12\x0b\n\x03Key\x18\x07 \x01(\x0c\x12\x0c\n\x04\x41\x43ME\x18\x08 \x01(\x08\x12\x12\n\nPersistent\x18\t \x01(\x08\x12\x12\n\nEnforceOTP\x18\n \x01(\x08\x12\x17\n\x0fLongPollTimeout\x18\x0b \x01(\x03\x12\x16\n\x0eLongPollJitter\x18\x0c \x01(\x03\x12\x15\n\rRandomizeJARM\x18\r \x01(\x08\"E\n\rNamedPipesReq\x12\x10\n\x08PipeName\x18\x10 \x01(\t\x12\"\n\x07Request\x18\t \x01(\x0b\x32\x11.commonpb.Request\"P\n\nNamedPipes\x12\x0f\n\x07Success\x18\x01 \x01(\x08\x12\x0b\n\x03\x45rr\x18\x02 \x01(\t\x12$\n\x08Response\x18\t \x01(\x0b\x32\x12.commonpb.Response\"B\n\x0bTCPPivotReq\x12\x0f\n\x07\x41\x64\x64ress\x18\x10 \x01(\t\x12\"\n\x07Request\x18\t \x01(\x0b\x32\x11.commonpb.Request\"N\n\x08TCPPivot\x12\x0f\n\x07Success\x18\x01 \x01(\x08\x12\x0b\n\x03\x45rr\x18\x02 \x01(\t\x12$\n\x08Response\x18\t \x01(\x0b\x32\x12.commonpb.Response\"\x1d\n\x0cHTTPListener\x12\r\n\x05JobID\x18\x01 \x01(\r\"/\n\x08Sessions\x12#\n\x08Sessions\x18\x01 \x03(\x0b\x32\x11.clientpb.Session\">\n\tRenameReq\x12\x11\n\tSessionID\x18\x01 \x01(\t\x12\x10\n\x08\x42\x65\x61\x63onID\x18\x02 \x01(\t\x12\x0c\n\x04Name\x18\x03 \x01(\t\"6\n\x0bGenerateReq\x12\'\n\x06\x43onfig\x18\x01 \x01(\x0b\x32\x17.clientpb.ImplantConfig\"(\n\x08Generate\x12\x1c\n\x04\x46ile\x18\x01 \x01(\x0b\x32\x0e.commonpb.File\"\x80\x01\n\x06MSFReq\x12\x0f\n\x07Payload\x18\x01 \x01(\t\x12\r\n\x05LHost\x18\x02 \x01(\t\x12\r\n\x05LPort\x18\x03 \x01(\r\x12\x0f\n\x07\x45ncoder\x18\x04 \x01(\t\x12\x12\n\nIterations\x18\x05 \x01(\x05\x12\"\n\x07Request\x18\t \x01(\x0b\x32\x11.commonpb.Request\"\x93\x01\n\x0cMSFRemoteReq\x12\x0f\n\x07Payload\x18\x01 \x01(\t\x12\r\n\x05LHost\x18\x02 \x01(\t\x12\r\n\x05LPort\x18\x03 \x01(\r\x12\x0f\n\x07\x45ncoder\x18\x04 \x01(\t\x12\x12\n\nIterations\x18\x05 \x01(\x05\x12\x0b\n\x03PID\x18\x08 \x01(\r\x12\"\n\x07Request\x18\t \x01(\x0b\x32\x11.commonpb.Request\"\x91\x01\n\x11StagerListenerReq\x12)\n\x08Protocol\x18\x01 \x01(\x0e\x32\x17.clientpb.StageProtocol\x12\x0c\n\x04Host\x18\x02 \x01(\t\x12\x0c\n\x04Port\x18\x03 \x01(\r\x12\x0c\n\x04\x44\x61ta\x18\x04 \x01(\x0c\x12\x0c\n\x04\x43\x65rt\x18\x05 \x01(\x0c\x12\x0b\n\x03Key\x18\x06 \x01(\x0c\x12\x0c\n\x04\x41\x43ME\x18\x07 \x01(\x08\"\x1f\n\x0eStagerListener\x12\r\n\x05JobID\x18\x01 \x01(\r\"H\n\x0fShellcodeRDIReq\x12\x0c\n\x04\x44\x61ta\x18\x01 \x01(\x0c\x12\x14\n\x0c\x46unctionName\x18\x02 \x01(\t\x12\x11\n\tArguments\x18\x03 \x01(\t\"\x1c\n\x0cShellcodeRDI\x12\x0c\n\x04\x44\x61ta\x18\x01 \x01(\x0c\"\x91\x01\n\x0cMsfStagerReq\x12\x0c\n\x04\x41rch\x18\x01 \x01(\t\x12\x0e\n\x06\x46ormat\x18\x02 \x01(\t\x12\x0c\n\x04Port\x18\x03 \x01(\r\x12\x0c\n\x04Host\x18\x04 \x01(\t\x12\n\n\x02OS\x18\x05 \x01(\t\x12)\n\x08Protocol\x18\x06 \x01(\x0e\x32\x17.clientpb.StageProtocol\x12\x10\n\x08\x42\x61\x64\x43hars\x18\x07 \x03(\t\")\n\tMsfStager\x12\x1c\n\x04\x46ile\x18\x01 \x01(\x0b\x32\x0e.commonpb.File\"s\n\x0cGetSystemReq\x12\x16\n\x0eHostingProcess\x18\x01 \x01(\t\x12\'\n\x06\x43onfig\x18\x02 \x01(\x0b\x32\x17.clientpb.ImplantConfig\x12\"\n\x07Request\x18\t \x01(\x0b\x32\x11.commonpb.Request\"f\n\nMigrateReq\x12\x0b\n\x03Pid\x18\x01 \x01(\r\x12\'\n\x06\x43onfig\x18\x02 \x01(\x0b\x32\x17.clientpb.ImplantConfig\x12\"\n\x07Request\x18\t \x01(\x0b\x32\x11.commonpb.Request\"5\n\x0f\x43reateTunnelReq\x12\"\n\x07Request\x18\t \x01(\x0b\x32\x11.commonpb.Request\"7\n\x0c\x43reateTunnel\x12\x11\n\tSessionID\x18\x01 \x01(\r\x12\x14\n\x08TunnelID\x18\x08 \x01(\x04\x42\x02\x30\x01\"J\n\x0e\x43loseTunnelReq\x12\x14\n\x08TunnelID\x18\x08 \x01(\x04\x42\x02\x30\x01\x12\"\n\x07Request\x18\t \x01(\x0b\x32\x11.commonpb.Request\"\x80\x01\n\x0fPivotGraphEntry\x12\x0e\n\x06PeerID\x18\x01 \x01(\x03\x12\"\n\x07Session\x18\x02 \x01(\x0b\x32\x11.clientpb.Session\x12\x0c\n\x04Name\x18\x03 \x01(\t\x12+\n\x08\x43hildren\x18\x04 \x03(\x0b\x32\x19.clientpb.PivotGraphEntry\"9\n\nPivotGraph\x12+\n\x08\x43hildren\x18\x01 \x03(\x0b\x32\x19.clientpb.PivotGraphEntry\"H\n\x06\x43lient\x12\n\n\x02ID\x18\x01 \x01(\r\x12\x0c\n\x04Name\x18\x02 \x01(\t\x12$\n\x08Operator\x18\x03 \x01(\x0b\x32\x12.clientpb.Operator\"\x97\x01\n\x05\x45vent\x12\x11\n\tEventType\x18\x01 \x01(\t\x12\"\n\x07Session\x18\x02 \x01(\x0b\x32\x11.clientpb.Session\x12\x1a\n\x03Job\x18\x03 \x01(\x0b\x32\r.clientpb.Job\x12 \n\x06\x43lient\x18\x04 \x01(\x0b\x32\x10.clientpb.Client\x12\x0c\n\x04\x44\x61ta\x18\x05 \x01(\x0c\x12\x0b\n\x03\x45rr\x18\x06 \x01(\t\"2\n\tOperators\x12%\n\tOperators\x18\x01 \x03(\x0b\x32\x12.clientpb.Operator\"(\n\x08Operator\x12\x0e\n\x06Online\x18\x01 \x01(\x08\x12\x0c\n\x04Name\x18\x02 \x01(\t\"R\n\nWebContent\x12\x0c\n\x04Path\x18\x01 \x01(\t\x12\x13\n\x0b\x43ontentType\x18\x02 \x01(\t\x12\x10\n\x04Size\x18\x03 \x01(\x04\x42\x02\x30\x01\x12\x0f\n\x07\x43ontent\x18\t \x01(\x0c\"\xa5\x01\n\x11WebsiteAddContent\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12;\n\x08\x43ontents\x18\x02 \x03(\x0b\x32).clientpb.WebsiteAddContent.ContentsEntry\x1a\x45\n\rContentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.clientpb.WebContent:\x02\x38\x01\"3\n\x14WebsiteRemoveContent\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\r\n\x05Paths\x18\x02 \x03(\t\"\x91\x01\n\x07Website\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x31\n\x08\x43ontents\x18\x02 \x03(\x0b\x32\x1f.clientpb.Website.ContentsEntry\x1a\x45\n\rContentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.clientpb.WebContent:\x02\x38\x01\"/\n\x08Websites\x12#\n\x08Websites\x18\x01 \x03(\x0b\x32\x11.clientpb.Website\"h\n\x0eWGClientConfig\x12\x14\n\x0cServerPubKey\x18\x01 \x01(\t\x12\x18\n\x10\x43lientPrivateKey\x18\x02 \x01(\t\x12\x14\n\x0c\x43lientPubKey\x18\x03 \x01(\t\x12\x10\n\x08\x43lientIP\x18\x04 \x01(\t\"<\n\nCredential\x12\x0c\n\x04User\x18\x02 \x01(\t\x12\x10\n\x08Password\x18\x03 \x01(\t\x12\x0e\n\x06\x41PIKey\x18\x04 \x01(\t\"\xe6\x01\n\x04Loot\x12 \n\x04Type\x18\x01 \x01(\x0e\x32\x12.clientpb.LootType\x12\x0e\n\x06LootID\x18\x02 \x01(\t\x12\x0c\n\x04Name\x18\x03 \x01(\t\x12\x30\n\x0e\x43redentialType\x18\x04 \x01(\x0e\x32\x18.clientpb.CredentialType\x12(\n\nCredential\x18\x05 \x01(\x0b\x32\x14.clientpb.Credential\x12$\n\x08\x46ileType\x18\x06 \x01(\x0e\x32\x12.clientpb.FileType\x12\x1c\n\x04\x46ile\x18\t \x01(\x0b\x32\x0e.commonpb.File\"\'\n\x07\x41llLoot\x12\x1c\n\x04Loot\x18\x01 \x03(\x0b\x32\x0e.clientpb.Loot\"1\n\x03IOC\x12\x0c\n\x04Path\x18\x01 \x01(\t\x12\x10\n\x08\x46ileHash\x18\x02 \x01(\t\x12\n\n\x02ID\x18\x03 \x01(\t\"\x1f\n\rExtensionData\x12\x0e\n\x06Output\x18\x01 \x01(\t\"\x89\x02\n\x04Host\x12\x10\n\x08Hostname\x18\x01 \x01(\t\x12\x10\n\x08HostUUID\x18\x02 \x01(\t\x12\x11\n\tOSVersion\x18\x03 \x01(\t\x12\x1b\n\x04IOCs\x18\x04 \x03(\x0b\x32\r.clientpb.IOC\x12\x38\n\rExtensionData\x18\x05 \x03(\x0b\x32!.clientpb.Host.ExtensionDataEntry\x12\x0e\n\x06Locale\x18\x06 \x01(\t\x12\x14\n\x0c\x46irstContact\x18\x07 \x01(\x03\x1aM\n\x12\x45xtensionDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.clientpb.ExtensionData:\x02\x38\x01\")\n\x08\x41llHosts\x12\x1d\n\x05Hosts\x18\x01 \x03(\x0b\x32\x0e.clientpb.Host\"\xa2\x01\n\x0c\x44llHijackReq\x12\x18\n\x10ReferenceDLLPath\x18\x01 \x01(\t\x12\x16\n\x0eTargetLocation\x18\x02 \x01(\t\x12\x14\n\x0cReferenceDLL\x18\x03 \x01(\x0c\x12\x11\n\tTargetDLL\x18\x04 \x01(\x0c\x12\x13\n\x0bProfileName\x18\x05 \x01(\t\x12\"\n\x07Request\x18\t \x01(\x0b\x32\x11.commonpb.Request\"1\n\tDllHijack\x12$\n\x08Response\x18\t \x01(\x0b\x32\x12.commonpb.Response\"\xaf\x01\n\x12ShellcodeEncodeReq\x12+\n\x07\x45ncoder\x18\x01 \x01(\x0e\x32\x1a.clientpb.ShellcodeEncoder\x12\x14\n\x0c\x41rchitecture\x18\x02 \x01(\t\x12\x12\n\nIterations\x18\x03 \x01(\r\x12\x10\n\x08\x42\x61\x64\x43hars\x18\x04 \x01(\x0c\x12\x0c\n\x04\x44\x61ta\x18\x08 \x01(\x0c\x12\"\n\x07Request\x18\t \x01(\x0b\x32\x11.commonpb.Request\"E\n\x0fShellcodeEncode\x12\x0c\n\x04\x44\x61ta\x18\x08 \x01(\x0c\x12$\n\x08Response\x18\t \x01(\x0b\x32\x12.commonpb.Response\"\xa1\x01\n\x13ShellcodeEncoderMap\x12=\n\x08\x45ncoders\x18\x01 \x03(\x0b\x32+.clientpb.ShellcodeEncoderMap.EncodersEntry\x1aK\n\rEncodersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0e\x32\x1a.clientpb.ShellcodeEncoder:\x02\x38\x01*X\n\x0cOutputFormat\x12\x0e\n\nSHARED_LIB\x10\x00\x12\r\n\tSHELLCODE\x10\x01\x12\x0e\n\nEXECUTABLE\x10\x02\x12\x0b\n\x07SERVICE\x10\x03\x12\x0c\n\x08\x45XTERNAL\x10\x04*-\n\rStageProtocol\x12\x07\n\x03TCP\x10\x00\x12\x08\n\x04HTTP\x10\x01\x12\t\n\x05HTTPS\x10\x02*.\n\x08LootType\x12\r\n\tLOOT_FILE\x10\x00\x12\x13\n\x0fLOOT_CREDENTIAL\x10\x01*M\n\x0e\x43redentialType\x12\x11\n\rNO_CREDENTIAL\x10\x00\x12\x11\n\rUSER_PASSWORD\x10\x01\x12\x0b\n\x07\x41PI_KEY\x10\x02\x12\x08\n\x04\x46ILE\x10\x03*-\n\x08\x46ileType\x12\x0b\n\x07NO_FILE\x10\x00\x12\n\n\x06\x42INARY\x10\x01\x12\x08\n\x04TEXT\x10\x02*&\n\x10ShellcodeEncoder\x12\x12\n\x0eSHIKATA_GA_NAI\x10\x00\x42/Z-github.com/bishopfox/sliver/protobuf/clientpbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'clientpb.client_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-github.com/bishopfox/sliver/protobuf/clientpb'
  _IMPLANTBUILDS_CONFIGSENTRY._options = None
  _IMPLANTBUILDS_CONFIGSENTRY._serialized_options = b'8\001'
  _CREATETUNNEL.fields_by_name['TunnelID']._options = None
  _CREATETUNNEL.fields_by_name['TunnelID']._serialized_options = b'0\001'
  _CLOSETUNNELREQ.fields_by_name['TunnelID']._options = None
  _CLOSETUNNELREQ.fields_by_name['TunnelID']._serialized_options = b'0\001'
  _WEBCONTENT.fields_by_name['Size']._options = None
  _WEBCONTENT.fields_by_name['Size']._serialized_options = b'0\001'
  _WEBSITEADDCONTENT_CONTENTSENTRY._options = None
  _WEBSITEADDCONTENT_CONTENTSENTRY._serialized_options = b'8\001'
  _WEBSITE_CONTENTSENTRY._options = None
  _WEBSITE_CONTENTSENTRY._serialized_options = b'8\001'
  _HOST_EXTENSIONDATAENTRY._options = None
  _HOST_EXTENSIONDATAENTRY._serialized_options = b'8\001'
  _SHELLCODEENCODERMAP_ENCODERSENTRY._options = None
  _SHELLCODEENCODERMAP_ENCODERSENTRY._serialized_options = b'8\001'
  _OUTPUTFORMAT._serialized_start=8560
  _OUTPUTFORMAT._serialized_end=8648
  _STAGEPROTOCOL._serialized_start=8650
  _STAGEPROTOCOL._serialized_end=8695
  _LOOTTYPE._serialized_start=8697
  _LOOTTYPE._serialized_end=8743
  _CREDENTIALTYPE._serialized_start=8745
  _CREDENTIALTYPE._serialized_end=8822
  _FILETYPE._serialized_start=8824
  _FILETYPE._serialized_end=8869
  _SHELLCODEENCODER._serialized_start=8871
  _SHELLCODEENCODER._serialized_end=8909
  _VERSION._serialized_start=59
  _VERSION._serialized_end=190
  _SESSION._serialized_start=193
  _SESSION._serialized_end=627
  _BEACON._serialized_start=630
  _BEACON._serialized_end=1131
  _BEACONS._serialized_start=1133
  _BEACONS._serialized_end=1177
  _BEACONTASK._serialized_start=1180
  _BEACONTASK._serialized_end=1349
  _BEACONTASKS._serialized_start=1351
  _BEACONTASKS._serialized_end=1419
  _IMPLANTC2._serialized_start=1421
  _IMPLANTC2._serialized_end=1480
  _IMPLANTCONFIG._serialized_start=1483
  _IMPLANTCONFIG._serialized_end=2403
  _EXTERNALIMPLANTCONFIG._serialized_start=2405
  _EXTERNALIMPLANTCONFIG._serialized_end=2502
  _EXTERNALIMPLANTBINARY._serialized_start=2504
  _EXTERNALIMPLANTBINARY._serialized_end=2596
  _IMPLANTBUILDS._serialized_start=2599
  _IMPLANTBUILDS._serialized_end=2742
  _IMPLANTBUILDS_CONFIGSENTRY._serialized_start=2671
  _IMPLANTBUILDS_CONFIGSENTRY._serialized_end=2742
  _COMPILERTARGET._serialized_start=2744
  _COMPILERTARGET._serialized_end=2830
  _CROSSCOMPILER._serialized_start=2832
  _CROSSCOMPILER._serialized_end=2922
  _COMPILER._serialized_start=2925
  _COMPILER._serialized_end=3111
  _DELETEREQ._serialized_start=3113
  _DELETEREQ._serialized_end=3138
  _DNSCANARY._serialized_start=3141
  _DNSCANARY._serialized_end=3270
  _CANARIES._serialized_start=3272
  _CANARIES._serialized_end=3321
  _UNIQUEWGIP._serialized_start=3323
  _UNIQUEWGIP._serialized_end=3347
  _IMPLANTPROFILE._serialized_start=3349
  _IMPLANTPROFILE._serialized_end=3420
  _IMPLANTPROFILES._serialized_start=3422
  _IMPLANTPROFILES._serialized_end=3483
  _REGENERATEREQ._serialized_start=3485
  _REGENERATEREQ._serialized_end=3521
  _JOB._serialized_start=3523
  _JOB._serialized_end=3624
  _JOBS._serialized_start=3626
  _JOBS._serialized_end=3663
  _KILLJOBREQ._serialized_start=3665
  _KILLJOBREQ._serialized_end=3689
  _KILLJOB._serialized_start=3691
  _KILLJOB._serialized_end=3729
  _MTLSLISTENERREQ._serialized_start=3731
  _MTLSLISTENERREQ._serialized_end=3796
  _MTLSLISTENER._serialized_start=3798
  _MTLSLISTENER._serialized_end=3827
  _WGLISTENERREQ._serialized_start=3829
  _WGLISTENERREQ._serialized_end=3939
  _WGLISTENER._serialized_start=3941
  _WGLISTENER._serialized_end=3968
  _DNSLISTENERREQ._serialized_start=3970
  _DNSLISTENERREQ._serialized_end=4089
  _DNSLISTENER._serialized_start=4091
  _DNSLISTENER._serialized_end=4119
  _HTTPLISTENERREQ._serialized_start=4122
  _HTTPLISTENERREQ._serialized_end=4369
  _NAMEDPIPESREQ._serialized_start=4371
  _NAMEDPIPESREQ._serialized_end=4440
  _NAMEDPIPES._serialized_start=4442
  _NAMEDPIPES._serialized_end=4522
  _TCPPIVOTREQ._serialized_start=4524
  _TCPPIVOTREQ._serialized_end=4590
  _TCPPIVOT._serialized_start=4592
  _TCPPIVOT._serialized_end=4670
  _HTTPLISTENER._serialized_start=4672
  _HTTPLISTENER._serialized_end=4701
  _SESSIONS._serialized_start=4703
  _SESSIONS._serialized_end=4750
  _RENAMEREQ._serialized_start=4752
  _RENAMEREQ._serialized_end=4814
  _GENERATEREQ._serialized_start=4816
  _GENERATEREQ._serialized_end=4870
  _GENERATE._serialized_start=4872
  _GENERATE._serialized_end=4912
  _MSFREQ._serialized_start=4915
  _MSFREQ._serialized_end=5043
  _MSFREMOTEREQ._serialized_start=5046
  _MSFREMOTEREQ._serialized_end=5193
  _STAGERLISTENERREQ._serialized_start=5196
  _STAGERLISTENERREQ._serialized_end=5341
  _STAGERLISTENER._serialized_start=5343
  _STAGERLISTENER._serialized_end=5374
  _SHELLCODERDIREQ._serialized_start=5376
  _SHELLCODERDIREQ._serialized_end=5448
  _SHELLCODERDI._serialized_start=5450
  _SHELLCODERDI._serialized_end=5478
  _MSFSTAGERREQ._serialized_start=5481
  _MSFSTAGERREQ._serialized_end=5626
  _MSFSTAGER._serialized_start=5628
  _MSFSTAGER._serialized_end=5669
  _GETSYSTEMREQ._serialized_start=5671
  _GETSYSTEMREQ._serialized_end=5786
  _MIGRATEREQ._serialized_start=5788
  _MIGRATEREQ._serialized_end=5890
  _CREATETUNNELREQ._serialized_start=5892
  _CREATETUNNELREQ._serialized_end=5945
  _CREATETUNNEL._serialized_start=5947
  _CREATETUNNEL._serialized_end=6002
  _CLOSETUNNELREQ._serialized_start=6004
  _CLOSETUNNELREQ._serialized_end=6078
  _PIVOTGRAPHENTRY._serialized_start=6081
  _PIVOTGRAPHENTRY._serialized_end=6209
  _PIVOTGRAPH._serialized_start=6211
  _PIVOTGRAPH._serialized_end=6268
  _CLIENT._serialized_start=6270
  _CLIENT._serialized_end=6342
  _EVENT._serialized_start=6345
  _EVENT._serialized_end=6496
  _OPERATORS._serialized_start=6498
  _OPERATORS._serialized_end=6548
  _OPERATOR._serialized_start=6550
  _OPERATOR._serialized_end=6590
  _WEBCONTENT._serialized_start=6592
  _WEBCONTENT._serialized_end=6674
  _WEBSITEADDCONTENT._serialized_start=6677
  _WEBSITEADDCONTENT._serialized_end=6842
  _WEBSITEADDCONTENT_CONTENTSENTRY._serialized_start=6773
  _WEBSITEADDCONTENT_CONTENTSENTRY._serialized_end=6842
  _WEBSITEREMOVECONTENT._serialized_start=6844
  _WEBSITEREMOVECONTENT._serialized_end=6895
  _WEBSITE._serialized_start=6898
  _WEBSITE._serialized_end=7043
  _WEBSITE_CONTENTSENTRY._serialized_start=6773
  _WEBSITE_CONTENTSENTRY._serialized_end=6842
  _WEBSITES._serialized_start=7045
  _WEBSITES._serialized_end=7092
  _WGCLIENTCONFIG._serialized_start=7094
  _WGCLIENTCONFIG._serialized_end=7198
  _CREDENTIAL._serialized_start=7200
  _CREDENTIAL._serialized_end=7260
  _LOOT._serialized_start=7263
  _LOOT._serialized_end=7493
  _ALLLOOT._serialized_start=7495
  _ALLLOOT._serialized_end=7534
  _IOC._serialized_start=7536
  _IOC._serialized_end=7585
  _EXTENSIONDATA._serialized_start=7587
  _EXTENSIONDATA._serialized_end=7618
  _HOST._serialized_start=7621
  _HOST._serialized_end=7886
  _HOST_EXTENSIONDATAENTRY._serialized_start=7809
  _HOST_EXTENSIONDATAENTRY._serialized_end=7886
  _ALLHOSTS._serialized_start=7888
  _ALLHOSTS._serialized_end=7929
  _DLLHIJACKREQ._serialized_start=7932
  _DLLHIJACKREQ._serialized_end=8094
  _DLLHIJACK._serialized_start=8096
  _DLLHIJACK._serialized_end=8145
  _SHELLCODEENCODEREQ._serialized_start=8148
  _SHELLCODEENCODEREQ._serialized_end=8323
  _SHELLCODEENCODE._serialized_start=8325
  _SHELLCODEENCODE._serialized_end=8394
  _SHELLCODEENCODERMAP._serialized_start=8397
  _SHELLCODEENCODERMAP._serialized_end=8558
  _SHELLCODEENCODERMAP_ENCODERSENTRY._serialized_start=8483
  _SHELLCODEENCODERMAP_ENCODERSENTRY._serialized_end=8558
# @@protoc_insertion_point(module_scope)
