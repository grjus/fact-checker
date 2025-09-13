import { NodejsFunctionProps } from 'aws-cdk-lib/aws-lambda-nodejs'
import { Runtime } from 'aws-cdk-lib/aws-lambda'
import { join } from 'path'

export enum MainTable {
    PK = 'pk',
    SK = 'sk',
    TIMESTAMP = 'timestamp',
    TIMESTAMP_NAME = 'timestampIndex'
}

export const awsSdkModuleName = '@aws-sdk'

export const globalLambdaProps: Partial<NodejsFunctionProps> = {
    runtime: Runtime.NODEJS_22_X,
    depsLockFilePath: join('lib', 'package-lock.json')
}
