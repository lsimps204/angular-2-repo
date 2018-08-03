FROM nginx:alpine

COPY nginx.conf /etc/nginx/nginx.conf

WORKDIR /usr/share/nginx/html

# Copy the compiled source code to the WORKDIR. Code should be precompiled before building the container
COPY dist/udemy .