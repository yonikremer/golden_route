FROM node:14

WORKDIR /golden_route/frontend

COPY /frontend/package.json ./
COPY /frontend/package-lock.json ./
COPY /frontend/public ./public
COPY /frontend/src ./src

RUN npm install

COPY . .

EXPOSE 3000

RUN npm run build
# install serve
RUN npm install -g serve
RUN serve -s build