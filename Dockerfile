FROM alpine:3.16

RUN  py -m ensurepip --upgrade\
    && pip install PyPDF2:2.7

CMD ["bash"]