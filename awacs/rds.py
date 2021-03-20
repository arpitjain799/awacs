# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon RDS'
prefix = 'rds'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddRoleToDBCluster = Action('AddRoleToDBCluster')
AddRoleToDBInstance = Action('AddRoleToDBInstance')
AddSourceIdentifierToSubscription = \
    Action('AddSourceIdentifierToSubscription')
AddTagsToResource = Action('AddTagsToResource')
ApplyPendingMaintenanceAction = Action('ApplyPendingMaintenanceAction')
AuthorizeDBSecurityGroupIngress = \
    Action('AuthorizeDBSecurityGroupIngress')
BacktrackDBCluster = Action('BacktrackDBCluster')
CancelExportTask = Action('CancelExportTask')
CopyDBClusterParameterGroup = Action('CopyDBClusterParameterGroup')
CopyDBClusterSnapshot = Action('CopyDBClusterSnapshot')
CopyDBParameterGroup = Action('CopyDBParameterGroup')
CopyDBSnapshot = Action('CopyDBSnapshot')
CopyOptionGroup = Action('CopyOptionGroup')
CreateDBCluster = Action('CreateDBCluster')
CreateDBClusterEndpoint = Action('CreateDBClusterEndpoint')
CreateDBClusterParameterGroup = Action('CreateDBClusterParameterGroup')
CreateDBClusterSnapshot = Action('CreateDBClusterSnapshot')
CreateDBInstance = Action('CreateDBInstance')
CreateDBInstanceReadReplica = Action('CreateDBInstanceReadReplica')
CreateDBParameterGroup = Action('CreateDBParameterGroup')
CreateDBProxy = Action('CreateDBProxy')
CreateDBProxyEndpoint = Action('CreateDBProxyEndpoint')
CreateDBSecurityGroup = Action('CreateDBSecurityGroup')
CreateDBSnapshot = Action('CreateDBSnapshot')
CreateDBSubnetGroup = Action('CreateDBSubnetGroup')
CreateEventSubscription = Action('CreateEventSubscription')
CreateGlobalCluster = Action('CreateGlobalCluster')
CreateOptionGroup = Action('CreateOptionGroup')
CrossRegionCommunication = Action('CrossRegionCommunication')
DeleteDBCluster = Action('DeleteDBCluster')
DeleteDBClusterEndpoint = Action('DeleteDBClusterEndpoint')
DeleteDBClusterParameterGroup = Action('DeleteDBClusterParameterGroup')
DeleteDBClusterSnapshot = Action('DeleteDBClusterSnapshot')
DeleteDBInstance = Action('DeleteDBInstance')
DeleteDBInstanceAutomatedBackup = \
    Action('DeleteDBInstanceAutomatedBackup')
DeleteDBParameterGroup = Action('DeleteDBParameterGroup')
DeleteDBProxy = Action('DeleteDBProxy')
DeleteDBProxyEndpoint = Action('DeleteDBProxyEndpoint')
DeleteDBSecurityGroup = Action('DeleteDBSecurityGroup')
DeleteDBSnapshot = Action('DeleteDBSnapshot')
DeleteDBSubnetGroup = Action('DeleteDBSubnetGroup')
DeleteEventSubscription = Action('DeleteEventSubscription')
DeleteGlobalCluster = Action('DeleteGlobalCluster')
DeleteOptionGroup = Action('DeleteOptionGroup')
DeregisterDBProxyTargets = Action('DeregisterDBProxyTargets')
DescribeAccountAttributes = Action('DescribeAccountAttributes')
DescribeCertificates = Action('DescribeCertificates')
DescribeDBClusterBacktracks = Action('DescribeDBClusterBacktracks')
DescribeDBClusterEndpoints = Action('DescribeDBClusterEndpoints')
DescribeDBClusterParameterGroups = \
    Action('DescribeDBClusterParameterGroups')
DescribeDBClusterParameters = Action('DescribeDBClusterParameters')
DescribeDBClusterSnapshotAttributes = \
    Action('DescribeDBClusterSnapshotAttributes')
DescribeDBClusterSnapshots = Action('DescribeDBClusterSnapshots')
DescribeDBClusters = Action('DescribeDBClusters')
DescribeDBEngineVersions = Action('DescribeDBEngineVersions')
DescribeDBInstanceAutomatedBackups = \
    Action('DescribeDBInstanceAutomatedBackups')
DescribeDBInstances = Action('DescribeDBInstances')
DescribeDBLogFiles = Action('DescribeDBLogFiles')
DescribeDBParameterGroups = Action('DescribeDBParameterGroups')
DescribeDBParameters = Action('DescribeDBParameters')
DescribeDBProxies = Action('DescribeDBProxies')
DescribeDBProxyEndpoints = Action('DescribeDBProxyEndpoints')
DescribeDBProxyTargetGroups = Action('DescribeDBProxyTargetGroups')
DescribeDBProxyTargets = Action('DescribeDBProxyTargets')
DescribeDBSecurityGroups = Action('DescribeDBSecurityGroups')
DescribeDBSnapshotAttributes = Action('DescribeDBSnapshotAttributes')
DescribeDBSnapshots = Action('DescribeDBSnapshots')
DescribeDBSubnetGroups = Action('DescribeDBSubnetGroups')
DescribeEngineDefaultClusterParameters = \
    Action('DescribeEngineDefaultClusterParameters')
DescribeEngineDefaultParameters = \
    Action('DescribeEngineDefaultParameters')
DescribeEventCategories = Action('DescribeEventCategories')
DescribeEventSubscriptions = Action('DescribeEventSubscriptions')
DescribeEvents = Action('DescribeEvents')
DescribeExportTasks = Action('DescribeExportTasks')
DescribeGlobalClusters = Action('DescribeGlobalClusters')
DescribeOptionGroupOptions = Action('DescribeOptionGroupOptions')
DescribeOptionGroups = Action('DescribeOptionGroups')
DescribeOrderableDBInstanceOptions = \
    Action('DescribeOrderableDBInstanceOptions')
DescribePendingMaintenanceActions = \
    Action('DescribePendingMaintenanceActions')
DescribeReservedDBInstances = Action('DescribeReservedDBInstances')
DescribeReservedDBInstancesOfferings = \
    Action('DescribeReservedDBInstancesOfferings')
DescribeSourceRegions = Action('DescribeSourceRegions')
DescribeValidDBInstanceModifications = \
    Action('DescribeValidDBInstanceModifications')
DownloadCompleteDBLogFile = Action('DownloadCompleteDBLogFile')
DownloadDBLogFilePortion = Action('DownloadDBLogFilePortion')
FailoverDBCluster = Action('FailoverDBCluster')
FailoverGlobalCluster = Action('FailoverGlobalCluster')
ListTagsForResource = Action('ListTagsForResource')
ModifyCurrentDBClusterCapacity = Action('ModifyCurrentDBClusterCapacity')
ModifyDBCluster = Action('ModifyDBCluster')
ModifyDBClusterEndpoint = Action('ModifyDBClusterEndpoint')
ModifyDBClusterParameterGroup = Action('ModifyDBClusterParameterGroup')
ModifyDBClusterSnapshotAttribute = \
    Action('ModifyDBClusterSnapshotAttribute')
ModifyDBInstance = Action('ModifyDBInstance')
ModifyDBParameterGroup = Action('ModifyDBParameterGroup')
ModifyDBProxy = Action('ModifyDBProxy')
ModifyDBProxyEndpoint = Action('ModifyDBProxyEndpoint')
ModifyDBProxyTargetGroup = Action('ModifyDBProxyTargetGroup')
ModifyDBSnapshot = Action('ModifyDBSnapshot')
ModifyDBSnapshotAttribute = Action('ModifyDBSnapshotAttribute')
ModifyDBSubnetGroup = Action('ModifyDBSubnetGroup')
ModifyEventSubscription = Action('ModifyEventSubscription')
ModifyGlobalCluster = Action('ModifyGlobalCluster')
ModifyOptionGroup = Action('ModifyOptionGroup')
PromoteReadReplica = Action('PromoteReadReplica')
PromoteReadReplicaDBCluster = Action('PromoteReadReplicaDBCluster')
PurchaseReservedDBInstancesOffering = \
    Action('PurchaseReservedDBInstancesOffering')
RebootDBInstance = Action('RebootDBInstance')
RegisterDBProxyTargets = Action('RegisterDBProxyTargets')
RemoveFromGlobalCluster = Action('RemoveFromGlobalCluster')
RemoveRoleFromDBCluster = Action('RemoveRoleFromDBCluster')
RemoveRoleFromDBInstance = Action('RemoveRoleFromDBInstance')
RemoveSourceIdentifierFromSubscription = \
    Action('RemoveSourceIdentifierFromSubscription')
RemoveTagsFromResource = Action('RemoveTagsFromResource')
ResetDBClusterParameterGroup = Action('ResetDBClusterParameterGroup')
ResetDBParameterGroup = Action('ResetDBParameterGroup')
RestoreDBClusterFromS3 = Action('RestoreDBClusterFromS3')
RestoreDBClusterFromSnapshot = Action('RestoreDBClusterFromSnapshot')
RestoreDBClusterToPointInTime = Action('RestoreDBClusterToPointInTime')
RestoreDBInstanceFromDBSnapshot = \
    Action('RestoreDBInstanceFromDBSnapshot')
RestoreDBInstanceFromS3 = Action('RestoreDBInstanceFromS3')
RestoreDBInstanceToPointInTime = Action('RestoreDBInstanceToPointInTime')
RevokeDBSecurityGroupIngress = Action('RevokeDBSecurityGroupIngress')
StartActivityStream = Action('StartActivityStream')
StartDBCluster = Action('StartDBCluster')
StartDBInstance = Action('StartDBInstance')
StartExportTask = Action('StartExportTask')
StopActivityStream = Action('StopActivityStream')
StopDBCluster = Action('StopDBCluster')
StopDBInstance = Action('StopDBInstance')
