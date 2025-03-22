from actors.repository import ActorRepository   

class ActorService:
    
    def __init__(self):
        self.actor_repository = ActorRepository()

    def get_actors(self):
        return self.actor_repository.get_actors()
    
    #aqui eu passo o que for necessário para criar um novo actor, nesse caso é name, birthday e nationality, diferente de genres
    def create_actors(self, name, birthday, nationality):
        actor = dict(
            name=name,
            birthday=birthday,
            nationality=nationality,
        )
        return self.actor_repository.create_actor(actor)