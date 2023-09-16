# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory inside the container
WORKDIR /client

# Copy package.json and package-lock.json (or yarn.lock if you use Yarn)
COPY package*.json ./

# Install project dependencies
RUN npm install
RUN npm install vue-router

# Copy the entire project into the container
COPY . .

# Build the Vue.js project with Vite (change the build command if needed)
RUN npm run build

# Expose the port that your application will run on (the default is 3000 for Vite)
EXPOSE 5173

# Define the command to start your application (change this to match your setup)
CMD ["npm", "run", "dev", "--","--port","5173","--host"]
