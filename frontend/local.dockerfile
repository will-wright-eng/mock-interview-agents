FROM node:18-alpine

# Next.js collects telemetry data by default, which you can disable by setting the environment variable below if you prefer
ENV NEXT_TELEMETRY_DISABLED 1

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .
