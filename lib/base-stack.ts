import { Stack, StackProps } from 'aws-cdk-lib'
import { Construct } from 'constructs'
import { EnvConfig } from './env.types'

export class BaseStack extends Stack {
    constructor(scope: Construct, id: string, {}: StackProps & EnvConfig) {
        super(scope, id)
    }
}
