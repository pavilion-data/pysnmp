#
# This file is part of pysnmp software.
#
# Copyright (c) 2005-2016, Ilya Etingof <ilya@glas.net>
# License: http://pysnmp.sf.net/license.html
#
# PySNMP MIB module RFC1158-MIB (http://pysnmp.sf.net)
# It is a stripped version of MIB that contains only symbols that is
# unique to SMIv1 and have no analogues in SMIv2
#
(Integer, ObjectIdentifier, OctetString,) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier",
                                                                     "OctetString")
(NamedValues,) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
(ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint,
 ValueRangeConstraint,) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint",
                                                   "ConstraintsIntersection", "ValueSizeConstraint",
                                                   "ValueRangeConstraint")
(Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, IpAddress, TimeTicks, iso, Gauge32, MibIdentifier,
 Bits, Counter32,) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow",
                                              "MibTableColumn", "mib-2", "IpAddress", "TimeTicks", "iso", "Gauge32",
                                              "MibIdentifier", "Bits", "Counter32")
(DisplayString,) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")
at = MibIdentifier((1, 3, 6, 1, 2, 1, 3))
ip = MibIdentifier((1, 3, 6, 1, 2, 1, 4))
egp = MibIdentifier((1, 3, 6, 1, 2, 1, 8))
atTable = MibTable((1, 3, 6, 1, 2, 1, 3, 1)).setMaxAccess("readwrite")
atEntry = MibTableRow((1, 3, 6, 1, 2, 1, 3, 1, 1)).setMaxAccess("readwrite")
atIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
atPhysAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 3, 1, 1, 2), OctetString()).setMaxAccess("readwrite")
atNetAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 3, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
ipRouteTable = MibTable((1, 3, 6, 1, 2, 1, 4, 21))
ipRouteEntry = MibTableRow((1, 3, 6, 1, 2, 1, 4, 21, 1)).setIndexNames((0, "RFC1213-MIB", "ipRouteDest"))
ipRouteDest = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 21, 1, 1), IpAddress()).setMaxAccess("readwrite")
ipRouteIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 21, 1, 2), Integer32()).setMaxAccess("readwrite")
ipRouteMetric1 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 21, 1, 3), Integer32()).setMaxAccess("readwrite")
ipRouteMetric2 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 21, 1, 4), Integer32()).setMaxAccess("readwrite")
ipRouteMetric3 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 21, 1, 5), Integer32()).setMaxAccess("readwrite")
ipRouteMetric4 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 21, 1, 6), Integer32()).setMaxAccess("readwrite")
ipRouteNextHop = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 21, 1, 7), IpAddress()).setMaxAccess("readwrite")
ipRouteType = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 21, 1, 8),
                             Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, )).clone(
                                 namedValues=NamedValues(("other", 1), ("invalid", 2), ("direct", 3),
                                                         ("indirect", 4), ))).setMaxAccess("readwrite")
ipRouteProto = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 21, 1, 9), Integer32().subtype(
    subtypeSpec=SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, )).clone(
    namedValues=NamedValues(("other", 1), ("local", 2), ("netmgmt", 3), ("icmp", 4), ("egp", 5), ("ggp", 6),
                            ("hello", 7), ("rip", 8), ("is-is", 9), ("es-is", 10), ("ciscoIgrp", 11), ("bbnSpfIgp", 12),
                            ("ospf", 13), ("bgp", 14), ))).setMaxAccess("readonly")
ipRouteAge = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 21, 1, 10), Integer32()).setMaxAccess("readwrite")
ipRouteMask = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 21, 1, 11), IpAddress()).setMaxAccess("readwrite")
ipRouteMetric5 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 21, 1, 12), Integer32()).setMaxAccess("readwrite")
ipRouteInfo = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 21, 1, 13), ObjectIdentifier()).setMaxAccess("readonly")
ipRoutingDiscards = MibScalar((1, 3, 6, 1, 2, 1, 4, 23), Counter32()).setMaxAccess("readonly")
egpInMsgs = MibScalar((1, 3, 6, 1, 2, 1, 8, 1), Counter32()).setMaxAccess("readonly")
egpInErrors = MibScalar((1, 3, 6, 1, 2, 1, 8, 2), Counter32()).setMaxAccess("readonly")
egpOutMsgs = MibScalar((1, 3, 6, 1, 2, 1, 8, 3), Counter32()).setMaxAccess("readonly")
egpOutErrors = MibScalar((1, 3, 6, 1, 2, 1, 8, 4), Counter32()).setMaxAccess("readonly")
egpNeighTable = MibTable((1, 3, 6, 1, 2, 1, 8, 5), )
egpNeighEntry = MibTableRow((1, 3, 6, 1, 2, 1, 8, 5, 1), ).setIndexNames((0, "RFC1213-MIB", "egpNeighAddr"))
egpNeighState = MibTableColumn((1, 3, 6, 1, 2, 1, 8, 5, 1, 1),
                               Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, 5, )).clone(
                                   namedValues=NamedValues(("idle", 1), ("acquisition", 2), ("down", 3), ("up", 4),
                                                           ("cease", 5), ))).setMaxAccess("readonly")
egpNeighAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 8, 5, 1, 2), IpAddress()).setMaxAccess("readonly")
egpNeighAs = MibTableColumn((1, 3, 6, 1, 2, 1, 8, 5, 1, 3), Integer32()).setMaxAccess("readonly")
egpNeighInMsgs = MibTableColumn((1, 3, 6, 1, 2, 1, 8, 5, 1, 4), Counter32()).setMaxAccess("readonly")
egpNeighInErrs = MibTableColumn((1, 3, 6, 1, 2, 1, 8, 5, 1, 5), Counter32()).setMaxAccess("readonly")
egpNeighOutMsgs = MibTableColumn((1, 3, 6, 1, 2, 1, 8, 5, 1, 6), Counter32()).setMaxAccess("readonly")
egpNeighOutErrs = MibTableColumn((1, 3, 6, 1, 2, 1, 8, 5, 1, 7), Counter32()).setMaxAccess("readonly")
egpNeighInErrMsgs = MibTableColumn((1, 3, 6, 1, 2, 1, 8, 5, 1, 8), Counter32()).setMaxAccess("readonly")
egpNeighOutErrMsgs = MibTableColumn((1, 3, 6, 1, 2, 1, 8, 5, 1, 9), Counter32()).setMaxAccess("readonly")
egpNeighStateUps = MibTableColumn((1, 3, 6, 1, 2, 1, 8, 5, 1, 10), Counter32()).setMaxAccess("readonly")
egpNeighStateDowns = MibTableColumn((1, 3, 6, 1, 2, 1, 8, 5, 1, 11), Counter32()).setMaxAccess("readonly")
egpNeighIntervalHello = MibTableColumn((1, 3, 6, 1, 2, 1, 8, 5, 1, 12), Integer32()).setMaxAccess("readonly")
egpNeighIntervalPoll = MibTableColumn((1, 3, 6, 1, 2, 1, 8, 5, 1, 13), Integer32()).setMaxAccess("readonly")
egpNeighMode = MibTableColumn((1, 3, 6, 1, 2, 1, 8, 5, 1, 14),
                              Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                  namedValues=NamedValues(("active", 1), ("passive", 2), ))).setMaxAccess("readonly")
egpNeighEventTrigger = MibTableColumn((1, 3, 6, 1, 2, 1, 8, 5, 1, 15),
                                      Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                          namedValues=NamedValues(("start", 1), ("stop", 2), ))).setMaxAccess(
    "readwrite")
egpAs = MibScalar((1, 3, 6, 1, 2, 1, 8, 6), Integer32()).setMaxAccess("readonly")
mibBuilder.exportSymbols("RFC1213-MIB", atPhysAddress=atPhysAddress, egpNeighMode=egpNeighMode, egpOutMsgs=egpOutMsgs,
                         ipRouteAge=ipRouteAge, ipRouteEntry=ipRouteEntry, egpNeighStateUps=egpNeighStateUps,
                         ipRouteInfo=ipRouteInfo, ipRoutingDiscards=ipRoutingDiscards, egpInErrors=egpInErrors,
                         egpOutErrors=egpOutErrors, ipRouteTable=ipRouteTable,
                         egpNeighEventTrigger=egpNeighEventTrigger, egpNeighTable=egpNeighTable,
                         ipRouteProto=ipRouteProto, egpNeighStateDowns=egpNeighStateDowns,
                         ipRouteNextHop=ipRouteNextHop, ipRouteMetric3=ipRouteMetric3, ipRouteMetric4=ipRouteMetric4,
                         ipRouteDest=ipRouteDest, ipRouteMetric2=ipRouteMetric2, egpNeighState=egpNeighState,
                         atNetAddress=atNetAddress, egpNeighOutErrs=egpNeighOutErrs, ipRouteIfIndex=ipRouteIfIndex,
                         atIfIndex=atIfIndex, ipRouteMask=ipRouteMask, ipRouteMetric5=ipRouteMetric5,
                         ipRouteType=ipRouteType, egpNeighIntervalPoll=egpNeighIntervalPoll,
                         egpNeighIntervalHello=egpNeighIntervalHello, atTable=atTable, ipRouteMetric1=ipRouteMetric1,
                         egpNeighInErrMsgs=egpNeighInErrMsgs, egpNeighInErrs=egpNeighInErrs, egpAs=egpAs,
                         egpNeighAddr=egpNeighAddr, egpNeighEntry=egpNeighEntry, egpNeighOutErrMsgs=egpNeighOutErrMsgs,
                         at=at, atEntry=atEntry, egpNeighOutMsgs=egpNeighOutMsgs, egpNeighInMsgs=egpNeighInMsgs,
                         egpInMsgs=egpInMsgs, egpNeighAs=egpNeighAs, egp=egp)
