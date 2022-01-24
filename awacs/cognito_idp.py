# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Cognito User Pools"
prefix = "cognito-idp"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddCustomAttributes = Action("AddCustomAttributes")
AdminAddUserToGroup = Action("AdminAddUserToGroup")
AdminConfirmSignUp = Action("AdminConfirmSignUp")
AdminCreateUser = Action("AdminCreateUser")
AdminDeleteUser = Action("AdminDeleteUser")
AdminDeleteUserAttributes = Action("AdminDeleteUserAttributes")
AdminDisableProviderForUser = Action("AdminDisableProviderForUser")
AdminDisableUser = Action("AdminDisableUser")
AdminEnableUser = Action("AdminEnableUser")
AdminForgetDevice = Action("AdminForgetDevice")
AdminGetDevice = Action("AdminGetDevice")
AdminGetUser = Action("AdminGetUser")
AdminInitiateAuth = Action("AdminInitiateAuth")
AdminLinkProviderForUser = Action("AdminLinkProviderForUser")
AdminListDevices = Action("AdminListDevices")
AdminListGroupsForUser = Action("AdminListGroupsForUser")
AdminListUserAuthEvents = Action("AdminListUserAuthEvents")
AdminRemoveUserFromGroup = Action("AdminRemoveUserFromGroup")
AdminResetUserPassword = Action("AdminResetUserPassword")
AdminRespondToAuthChallenge = Action("AdminRespondToAuthChallenge")
AdminSetUserMFAPreference = Action("AdminSetUserMFAPreference")
AdminSetUserPassword = Action("AdminSetUserPassword")
AdminSetUserSettings = Action("AdminSetUserSettings")
AdminUpdateAuthEventFeedback = Action("AdminUpdateAuthEventFeedback")
AdminUpdateDeviceStatus = Action("AdminUpdateDeviceStatus")
AdminUpdateUserAttributes = Action("AdminUpdateUserAttributes")
AdminUserGlobalSignOut = Action("AdminUserGlobalSignOut")
AssociateSoftwareToken = Action("AssociateSoftwareToken")
ChangePassword = Action("ChangePassword")
ConfirmDevice = Action("ConfirmDevice")
ConfirmForgotPassword = Action("ConfirmForgotPassword")
ConfirmSignUp = Action("ConfirmSignUp")
CreateGroup = Action("CreateGroup")
CreateIdentityProvider = Action("CreateIdentityProvider")
CreateResourceServer = Action("CreateResourceServer")
CreateUserImportJob = Action("CreateUserImportJob")
CreateUserPool = Action("CreateUserPool")
CreateUserPoolClient = Action("CreateUserPoolClient")
CreateUserPoolDomain = Action("CreateUserPoolDomain")
DeleteGroup = Action("DeleteGroup")
DeleteIdentityProvider = Action("DeleteIdentityProvider")
DeleteResourceServer = Action("DeleteResourceServer")
DeleteUser = Action("DeleteUser")
DeleteUserAttributes = Action("DeleteUserAttributes")
DeleteUserPool = Action("DeleteUserPool")
DeleteUserPoolClient = Action("DeleteUserPoolClient")
DeleteUserPoolDomain = Action("DeleteUserPoolDomain")
DescribeIdentityProvider = Action("DescribeIdentityProvider")
DescribeResourceServer = Action("DescribeResourceServer")
DescribeRiskConfiguration = Action("DescribeRiskConfiguration")
DescribeUserImportJob = Action("DescribeUserImportJob")
DescribeUserPool = Action("DescribeUserPool")
DescribeUserPoolClient = Action("DescribeUserPoolClient")
DescribeUserPoolDomain = Action("DescribeUserPoolDomain")
ForgetDevice = Action("ForgetDevice")
ForgotPassword = Action("ForgotPassword")
GetCSVHeader = Action("GetCSVHeader")
GetDevice = Action("GetDevice")
GetGroup = Action("GetGroup")
GetIdentityProviderByIdentifier = Action("GetIdentityProviderByIdentifier")
GetSigningCertificate = Action("GetSigningCertificate")
GetUICustomization = Action("GetUICustomization")
GetUser = Action("GetUser")
GetUserAttributeVerificationCode = Action("GetUserAttributeVerificationCode")
GetUserPoolMfaConfig = Action("GetUserPoolMfaConfig")
GlobalSignOut = Action("GlobalSignOut")
InitiateAuth = Action("InitiateAuth")
ListDevices = Action("ListDevices")
ListGroups = Action("ListGroups")
ListIdentityProviders = Action("ListIdentityProviders")
ListResourceServers = Action("ListResourceServers")
ListTagsForResource = Action("ListTagsForResource")
ListUserImportJobs = Action("ListUserImportJobs")
ListUserPoolClients = Action("ListUserPoolClients")
ListUserPools = Action("ListUserPools")
ListUsers = Action("ListUsers")
ListUsersInGroup = Action("ListUsersInGroup")
ResendConfirmationCode = Action("ResendConfirmationCode")
RespondToAuthChallenge = Action("RespondToAuthChallenge")
RevokeToken = Action("RevokeToken")
SetRiskConfiguration = Action("SetRiskConfiguration")
SetUICustomization = Action("SetUICustomization")
SetUserMFAPreference = Action("SetUserMFAPreference")
SetUserPoolMfaConfig = Action("SetUserPoolMfaConfig")
SetUserSettings = Action("SetUserSettings")
SignUp = Action("SignUp")
StartUserImportJob = Action("StartUserImportJob")
StopUserImportJob = Action("StopUserImportJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAuthEventFeedback = Action("UpdateAuthEventFeedback")
UpdateDeviceStatus = Action("UpdateDeviceStatus")
UpdateGroup = Action("UpdateGroup")
UpdateIdentityProvider = Action("UpdateIdentityProvider")
UpdateResourceServer = Action("UpdateResourceServer")
UpdateUserAttributes = Action("UpdateUserAttributes")
UpdateUserPool = Action("UpdateUserPool")
UpdateUserPoolClient = Action("UpdateUserPoolClient")
UpdateUserPoolDomain = Action("UpdateUserPoolDomain")
VerifySoftwareToken = Action("VerifySoftwareToken")
VerifyUserAttribute = Action("VerifyUserAttribute")
