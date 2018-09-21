# openwhisk-pyohio
## Code and instructions for PyOhio 2018 session "Serverless? How About VENDORLESS?!"

### NOTE: This repo will be removed on July 1, 2019

## Want More?
* https://developer.redhat.com
* https://bit.ly/faas-tutorial
* https://learn.openshift.com/serverless

## Prerequisites
* [minishift](https://github.com/minishift/minishift)
* [OpenWhisk CLI](https://github.com/apache/incubator-openwhisk-cli) (wsk)
* [OpenWhisk on OpenShift](https://github.com/projectodd/openwhisk-openshift)

## Make sure `wsk` is in your path
(example):
```
export PATH=~/Downloads:$PATH
```

## Start OpenWhisk using minishift
```
minishift start --memory 8GB
eval $(minishift oc-env)
eval $(minishift docker-env)
cd openshift-openwhisk
./tools/travis/build.sh
cd ~/
```

## See list of actions
```
wsk -i action list
```

## Create hello function
```
wsk -i action create hello hello.py
```

## Run hello function
```
wsk -i action invoke hello --result
wsk -i action invoke hello --result  --param name 'Don'
```

## Run hello without immediate result
```
wsk -i action invoke # Note the activation id returned; it's used in the next step
wsk -i activation get {using activation id from previous step}
```

## Create qotd function
```
wsk -i action create qotd qotd.py
```

## Run QOTD function
```
wsk -i action invoke qotd --result
```

## Chaining Actions
```
wsk -i action create hello-and-quote --sequence hello,qotd
wsk -i action invoke hello-and-quote --result
wsk -i action invoke hello-and-quote --param name 'Fine person' --result
```

## Create a Web Action
```
wsk -i action create --web=true hello-web hello.py
WEB_URL=`wsk -i action get hello-web --url | awk 'FNR==2{print $1".json"}'` # # (1)
AUTH=`oc get secret whisk.auth -n openwhisk -o yaml | grep "system:" | awk '{print $2}'` # # (2)
curl -k $WEB_URL
```
## Want More?
* developer.redhat.com
* bit.ly/faas-tutorial
* https://learn.openshift.com/serverless

