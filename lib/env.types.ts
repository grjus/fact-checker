import { RetentionDays } from 'aws-cdk-lib/aws-logs'
import { RemovalPolicy } from 'aws-cdk-lib'

type LambdaLayerParams = Readonly<{
    parameterStoreName: string
    moduleName: string
}>

export type EnvConfig = Readonly<{
    logRetention: RetentionDays
    mainDynamoDbParams: DynamoDbParams
    removalPolicy: RemovalPolicy
    layers: LambdaLayers
    secretParams: NameVal
}>

type DynamoDbParams = {
    removalPolicy: RemovalPolicy
}

type LayerClient = 'axiosClientLayerParams' | 'geminiClientLayerParams'

export type LambdaLayers = Record<LayerClient, LambdaLayerParams>

export type NameVal = Readonly<{ name: string }>
