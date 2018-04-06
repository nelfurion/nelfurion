from django.shortcuts import render

projects = {
    'left': [
         {
            'media_url': 'http://localhost:8000/static/public/img/chatbot.jpg',
            'title': 'Thesis',
            'description': 'Leveraging Machine Learning and Natural \
             Language Processing the Jackson chatbot exploits the knowledge of Wikipedia to find answers for the hardest questions, while at the same \
             learning more about you.',
            'additional_info': '<p> Jackson earned me a Laureate title at the Bulgarian National IT Olypiad,  and also an excellent grade and compliments at ELSYS. </p>\
                                You can find Jackson here: \
                                    <a href="https://github.com/nelfurion/jackson" target="blank">Github</a> \
                                and my paper here: \
                                    <a href="https://drive.google.com/file/d/0B1L7B58PaEK6V2tGb2UzQ0tETDQ/view?usp=sharing" target="blank">Paper</a>.',
            'description_type': 'text',
            'additional_info_type': 'html',
            'background_image': 'http://localhost:8000/static/public/img/jackson.png',
         },
         {
            'media_url': 'http://localhost:8000/static/public/img/hacktues.png',
            'title': 'HackTues',
            'description': 'HackTUES is the first and the only Bulgarian high school Hackathon. Running for four consecutive years, \
                             HackTUES confronts students with the dificulties of building Software and Hardware in a real competitive \
                             business environment. Each year more and more students participate and more than 200 students took part in the 4th edition.',
            'description_type': 'text',
            'additional_info_type': 'html',
            'additional_info': '<p>Organizing it from ground zero, I played a big role building HackTUES and moving it from a dream, to a reality.</p> \
                                <p><a href="https://hacktues.com/" target="blank">HackTUES</a></p>',
            'background_image': 'http://localhost:8000/static/public/img/hacktues_back.jpg',
         },
         {
            'media_url': 'http://localhost:8000/static/public/img/consistorium.png',
            'title': 'Consistorium',
            'description': 'Consistorium is a sandbox survival game written in C++, SDL, Box2D. I played a part \
                            in building the application from scratch. I wrote well structured, loosely coupled, segregated modules. \
                            I took part in building both the project architecture, and the game\'s mechanics and gameplay.',
            'additional_info': '<p><a href="https://github.com/Consistorium/Consistorium" target="blank">Consistorium on Github</a></p>\
                                <p><a href="http://consistorium.wikia.com/wiki/Consistorium_Wikia" target="blank">Consistorium Wikia</a></p>',
            'additional_info_type': 'html',
         },
         {
            'media_url': 'http://localhost:8000/static/public/img/elsys.png',
            'title': 'Graduated the best professional technology high school in Bulgaria',
            'description': '<p>In the summer of 2017 I graduated the best professional technology high school in Bulgaria - \
                            <a href="http://elsys-bg.org/" target="blank">ELSYS</a>.</p>\
                            <p>\
                            That same year \
                            I built an amazing thesis project which not only took me to the national round of the Bulgarian National \
                            Olympiad of Information Technology, which I passed with excellence, earned me the title of Laureate of the olympiad, \
                            got me invited to the John Atanasoff national prize tournament, but also introduced me to the field \
                            of Natural Language Processing, earned me respect and an A grade on my final exam.\
                            </p>',
            'description_type': 'html',
            'additional_info': '<p>\
                                I studied many different aspects of Software Engineering - and Hardware - OOP, Embedded, Operating Systems \
                                WEB development, Databases, Entrepreneurship, Electronical elements, Analogue and Digital Circuitry, etc, \
                                and I graduated with excellence.\
                                </p>',
            'additional_info_type': 'html',
            'title_dark': True,
         }
    ], 'right': [
         {
            'media_url': 'http://localhost:8000/static/public/img/blog.png',
            'description': 'This is my blog, which I created recently. Here I share my thoughts, knowledge and interesting topics in Computer Science, Mathematics, Software and Hardware.',
            'title': 'Thoughts on Computer Science',
            'additional_info_type': 'html',
            'description_type': 'text',
            'additional_info': '<p><a href="https://smshsite.wordpress.com/" target="blank">Thougs on Computer Science</a></p>',
         },
         {
            'media_url': 'http://localhost:8000/static/public/img/intern.jpg',
            'background_image': 'http://localhost:8000/static/public/img/genes.png',
            'title': 'Extracting Gene Expression Data',
            'description': 'In 2016 I did an internship, describing how specific genes\' expressions vary for different age groups and parts of the brain. \
                            I processed tens of thousands of rows of data using Unsipervised Machine Learning and more specifically mini batch k-means clustering over a dataset of gene expressions \
                            in the brain of people to find which of them are related to autism.',
            'description_type': 'text',
            'background_image': 'http://localhost:8000/static/public/img/genes.png',
         },
         {
            'media_url': 'http://localhost:8000/static/public/img/hackfmi.jpg',
            'title': 'HackFMI',
            'description': 'I took part in the Sofia University Faculty of Mathematics and Informatics hackathon HackFMI\'s 2nd, 3rd and 4th editions, \
                            while I was still in high school. \
                            My team built 2 websites and a game written in C++, and won several sponsor prizes. \
                            Later it was forbidden for non-university students to participate, and then the idea of HackTUES was born, \
                            to transfer the atmosphere of the event to my high school.',
            'additional_info_type': 'html',
            'additional_info': '<p><a href="https://hackfmi.com/" target="blank">HackFMI</a></p>',
            'background_image': 'http://localhost:8000/static/public/img/hackfmi_back.jpg',
         },
         {
            'media_url': 'http://localhost:8000/static/public/img/telerik.png',
            'title': 'Graduated Telerik Software Academy 2016 Ninja Track',
            'description': '<p>While in high school I\'ve always stayde ahead of schedule. In 2015 I entered the Telerik Software Academy \
                            and in 2016 I graduated it\'s Ninja track, combining both WEB and Mobile modules. I earned all of the sertificates \
                            for the season.</p>',
            'description_type': 'html',
            'additional_info': '<div> \
                                The certificates show the different modules I have studied in Telerik: \
                                <p><a href="http://my.telerikacademy.com/certificates/View/1945/3046e402" target="blank">Telerik Academy Ninja Certificate</a></p> \
                                <p><a href="http://my.telerikacademy.com/certificates/View/1946/f995435f" target="blank">Javascript Developer Certificate</a></p> \
                                <p><a href="http://my.telerikacademy.com/certificates/View/1948/05733344" target="blank">Mobile Developer Certificate</a></p> \
                                <p><a href="http://my.telerikacademy.com/certificates/View/1947/dac59c00" target="blank">WEB Developer Certificate</a></p> \
                                <p><a href="http://my.telerikacademy.com/certificates/View/1561/b2f7da58" target="blank">C# Developer Certificate</a></p> \
                                </div>',
            'additional_info_type': 'html',
         }
    ]
}

more_projects = [{
        'title': 'WoahMe',
        'media_url': 'http://localhost:8000/static/public/img/woahme.png',
        'description': 'Android application for image sharing.',
        'link': {
            'url':'https://github.com/WoahMe/WoahMe',
            'title': 'WoahMe on Github',
        }
    }, {
        'title': 'Mobile Food Ordering',
        'media_url': 'http://localhost:8000/static/public/img/mobile_food_ordering.png',
        'description': 'Universal Windows Application for food ordering.',
        'link': {
            'url':'https://github.com/Windows-Applications-Captain-Cold/Mobile-Food-Ordering',
            'title': 'Mobile Food Ordering on Github',
        }
    }, {
        'title': 'Scacrifice',
        'media_url': 'http://localhost:8000/static/public/img/scacrifice.png',
        'description': 'A NativeScript stress relieval game.',
        'link': {
            'url':'https://github.com/NativeScriptTA/ScacrificeApp',
            'title': 'Scacrifice on Github',
        }
    }, {
        'title': 'Arduino-Pong',
        'media_url': 'http://localhost:8000/static/public/img/arduino_pong.jpeg',
        'description': 'Ping pong embedded project built using Arduino.',
        'link': {
            'url':'https://github.com/Computer-Architectures-Team/Arduino-Pong',
            'title': 'Arduino-Pong on Github',
        },
        'title_dark': True,
    }, {
        'title': 'RepoCounter',
        'media_url': 'http://localhost:8000/static/public/img/repo_counter.png',
        'description': 'Small script to build lines of code statistics for repositories.',
        'link': {
            'url':'https://github.com/TUES-ProjectTP/RepoCounter',
            'title': 'RepoCounter on Github',
        },
        'title_dark': True,
    },
]

def index(request):
    return render(request, 'public/index.html', {
        'projects': projects,
        'more_projects': more_projects
    })
