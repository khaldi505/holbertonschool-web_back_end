export default function handleResponseFromAPI(promise) {
  console.log('Got a response from the API')
  promise.then(function(){
    return({ status: 200, body: 'Success' })
  }).catch(function(){
    return( new Error())
  })
}
