module.exports = function(app)
{
     app.get('/',function(req,res){
        res.render('index.html')
     });
     app.get('/calendar',function(req,res){
        res.render('calendar.html');
    });
    app.get('/login',function(req,res){
        res.render('login.html');
    });
}