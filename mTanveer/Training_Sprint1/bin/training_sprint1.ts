#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { TrainingSprint1Stack } from '../lib/training_sprint1-stack';

const app = new cdk.App();
new TrainingSprint1Stack(app, 'TrainingSprint1Stack');
