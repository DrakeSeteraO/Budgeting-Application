FROM node:17-alpine
WORKDIR /app
COPY package*.json /app

RUN npm i --silent
RUN npm i -g react-scripts@5.0.1

COPY . ./

# Fix permissions for the node_modules directory
RUN mkdir -p node_modules/.cache && chmod -R 777 node_modules/.cache

EXPOSE 3000

CMD ["npm", "start"]