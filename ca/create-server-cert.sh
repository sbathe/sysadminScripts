#!/bin/bash
CN="$1"
openssl genrsa -out intermediate/private/${CN}.key.pem 2048
openssl req -config intermediate/openssl.cnf -key intermediate/private/${CN}.key.pem -new -sha256 -out intermediate/csr/${CN}.csr.pem
openssl ca -config intermediate/openssl.cnf -extensions server_cert -days 375 -notext -md sha256 -in intermediate/csr/${CN}.csr.pem -out intermediate/certs/${CN}.cert.pem
openssl pkcs12 -export -name ${CN}cert -in intermediate/certs/${CN}.cert.pem -inkey intermediate/private/${CN}.key.pem  -out ${CN}.p12
keytool -importkeystore -destkeystore ${CN}.jks -srckeystore ${CN}.p12 -srcstoretype pkcs12 -alias ${CN}cert
