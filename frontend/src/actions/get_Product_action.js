import axios from 'axios';

const getproducts=()=>{
return dispatch=>{
    dispatch(loading());
    
    axios.get('api/products/').then(res=>dispatch(fetcheddata(res.data)))
    .catch(()=>dispatch(errorfetch()))
}
}

const loading=()=>({
    type:'LOADING_PRODUCTS'
});

const fetcheddata=(data)=>({
    type:'FETCHED_PRODUCT_DATA',
    payload:data
});

const errorfetch=()=>({
    type:'FETCH_PRODUCT_ERROR'
});

export default getproducts
