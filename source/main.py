def function(*args, **kwargs) -> None:
    print(kwargs)
    
function({
    "name": 3,
    "p": 4
})
