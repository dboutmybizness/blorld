
live_server = ['gamelifestats.com','www.gamelifestats.com']

meta = {}
meta['live'] = False


class site_meta:
    def __init__(self, request):

        self.is_live = self.on_live_server(request)
        self.GA_prop = self.get_GA_prop()
        self.social_links = self.get_social_links()
        self.path = request.path
        self.desc = 'Elevate Your BBall Game is an android app that allows you to track your basketball game stats. It\'s a free experience without ads built by former players. Easy to upload a game, also includes clear instructions. Current features include Game Upload, Averages/Totals, Game by Game browser, Profile (scout,skills,and bio). Plans to add other recreational aspects of the active basketball player are already in the works. Hope you enjoy.'
        self.url = request.build_absolute_uri()
        self.live_url = 'http://gamelifestats.com' + self.path
        self.img_fb = 'http://' + request.META['SERVER_NAME'] + ':8080/static/img/social_icon.png'
        if self.is_live:
            self.img_fb = 'http://i.gamelifestats.com/static/img/social_icon.png'
        self.type = 'website'
        self.user = request.user
        if self.user.is_authenticated():
            self.profile = self.attach_player_profile()
        self.page_title = 'GameLifeStats.com - an interactive platform for basketball players, fans, and enthusiast'
        self.meta_description = 'GameLifeStats (GLS) is basketball community for players, coaches, parents, sports professionals, and other enthusiast.  Sports/basketball has played or actively plays a great role in our development.  We attempt to engage our community through mobile and web applications and blogs.'
        self.page_keywords = 'basketball, bball, youth basketball, game life stats, gamelifestats, gls'
        self.handle = '@gamelifestats'
        self.handle_creator = ''
        self.is_author = self.is_user_author()
        self.no_analytics = self.restrict_analytics()
        self.gls_fallback_img = 'teamgls_fallback_image.png'

    def on_live_server(self, r):
        live_server = ['gamelifestats.com','www.gamelifestats.com']
        return ( True if r.META['SERVER_NAME'] in live_server else False)

    def get_GA_prop(self):
        return ('UA-27456895-1' if self.is_live else 'UA-27456895-2')

    def get_social_links(self):
        return {
            'gplus' : 'https://plus.google.com/+Gamelifestatselevate',
            'gplus_author' : 'https://plus.google.com/+Gamelifestatselevate',
            'fb' : 'https://www.facebook.com/gamelifestats',
            'twitter' : 'https://twitter.com/gamelifestats',
            'youtube' : 'http://www.youtube.com/user/GameLifeStats',
            'instagram' : 'http://instagram.com/gamelifestats',
        }

    def is_user_author(self):
        if not self.user.is_authenticated():
	    return False
        from glsblog.models import Author
	ck_user = Author.objects.filter(user = self.user)
	return (True if ck_user else False)
	
    def restrict_analytics(self):
        if self.path.startswith('/cms/'):
            return True
        return False

    def attach_player_profile(self):
        from elevate.models import Player
        return Player.objects.get(user = self.user)
