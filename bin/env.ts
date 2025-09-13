import { RemovalPolicy, StackProps } from 'aws-cdk-lib'
import { EnvConfig } from '../lib/env.types'
import { RetentionDays } from 'aws-cdk-lib/aws-logs'

const DEFAULT_STACK_NAME = 'FactCheckerStack'
const TEST_STACK_NAME = 'FactCheckerTestStack'

type BaseConfig = StackProps & EnvConfig

export const env = (): Record<string, BaseConfig> => ({
    [DEFAULT_STACK_NAME]: {
        logRetention: RetentionDays.ONE_WEEK,
        mainDynamoDbParams: {
            removalPolicy: RemovalPolicy.RETAIN
        },
        removalPolicy: RemovalPolicy.RETAIN,

        layers: {
            axiosClientLayerParams: {
                parameterStoreName: '/fact-checker/lambda-layers/axios-client',
                moduleName: 'axios-client'
            },
            geminiClientLayerParams: {
                parameterStoreName: '/fact-checker/lambda-layers/gemini-client',
                moduleName: 'gemini-client'
            }
        },
        secretParams: {
            name: 'fact-checker/prod'
        }
    } satisfies BaseConfig,
    [TEST_STACK_NAME]: {
        logRetention: RetentionDays.ONE_WEEK,
        mainDynamoDbParams: {
            removalPolicy: RemovalPolicy.DESTROY
        },
        removalPolicy: RemovalPolicy.DESTROY,

        layers: {
            axiosClientLayerParams: {
                parameterStoreName: '/fact-checker/lambda-layers/axios-client',
                moduleName: 'axios-client'
            },
            geminiClientLayerParams: {
                parameterStoreName: '/fact-checker/lambda-layers/gemini-client',
                moduleName: 'gemini-client'
            }
        },
        secretParams: {
            name: 'fact-checker/prod'
        }
    } satisfies BaseConfig
})
