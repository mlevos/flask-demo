FROM python:3.9.5-alpine
LABEL email="mathias.levostre@gmail.com" 
LABEL author="Mathias LEVOSTRE"
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser
WORKDIR /home/appuser/
COPY --chown=appuser:appgroup dist/*.whl /home/appuser/
COPY --chown=appuser:appgroup entrypoint.sh /home/appuser/
RUN pip install gunicorn *.whl --no-cache-dir
EXPOSE 8080
CMD [ "./entrypoint.sh" ]