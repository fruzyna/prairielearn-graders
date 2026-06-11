FROM mcr.microsoft.com/devcontainers/java:25-trixie

# yarn's key breaks debian updates all the time I guess
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | gpg --dearmor > /usr/share/keyrings/yarn-archive-keyring.gpg

# install python
RUN apt update
RUN apt install -y python3

# clone framework and create tests directory
RUN git clone https://github.com/fruzyna/systemcore_framework.git /grader
RUN mkdir -p /grader/src/test
WORKDIR /grader

# copy in grader and start
COPY ./grade-subsystem.* /grader
RUN ./gradlew --configuration-cache build
ENTRYPOINT ["/grader/grade-subsystem.sh"]