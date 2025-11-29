from project.artifacts.base_artifact import BaseArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.base_collector import BaseCollector
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector

artifact_mapper = {"RenaissanceArtifact":RenaissanceArtifact
                   ,"ContemporaryArtifact":ContemporaryArtifact
                   }

collector_mapper = {"Museum":Museum
                   ,"PrivateCollector":PrivateCollector
                    }

class AuctionHouseManagerApp:
    artefacts_sold = 0
    def __init__(self):
        self.artifacts: list[BaseArtifact] = []
        self.collectors: list[BaseCollector] = []

    def artifact_exists(self,name):
        return next((a for a in self.artifacts if a.name == name),None)

    def collector_exists(self,name):
        return next((c for c in self.collectors if c.name == name),None)

    def register_artifact(self,artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        if artifact_type not in artifact_mapper:
            raise ValueError("Unknown artifact type!")

        artifact = self.artifact_exists(artifact_name)

        if artifact:
            raise ValueError(f"{artifact_name} has been already registered!")

        artifact = artifact_mapper[artifact_type](artifact_name,artifact_price,artifact_space)
        self.artifacts.append(artifact)
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self,collector_type: str, collector_name: str):
        if collector_type not in collector_mapper:
            raise ValueError("Unknown collector type!")

        collector = self.collector_exists(collector_name)

        if collector:
            raise ValueError(f"{collector_name} has been already registered!")

        collector = collector_mapper[collector_type](collector_name)
        self.collectors.append(collector)
        return f"{collector_name} is successfully registered as a {collector_type}."


    def perform_purchase(self,collector_name: str, artifact_name: str):
        collector = self.collector_exists(collector_name)

        if collector is None:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")

        artifact = self.artifact_exists(artifact_name)

        if artifact is None:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")

        if not collector.can_purchase(artifact.price,artifact.space_required):
            return "Purchase is impossible."

        self.artifacts.remove(artifact)
        self.artefacts_sold += 1

        collector.purchased_artifacts.append(artifact)
        collector.available_money -= artifact.price
        collector.available_space -= artifact.space_required

        return f"{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}."


    def remove_artifact(self,artifact_name: str):
        artefact = self.artifact_exists(artifact_name)

        if artefact is None:
            return "No such artifact."

        self.artifacts.remove(artefact)
        return f"Removed {artefact.artifact_information()}"


    def fundraising_campaigns(self,max_money: float):
        collectors: list[BaseCollector] = [c for c in self.collectors if c.available_money <= max_money]
        [c.increase_money() for c in collectors]

        return f"{len(collectors)} collector/s increased their available money."


    def get_auction_report(self):
        result = ['**Auction statistics**',f'Total number of sold artifacts: {self.artefacts_sold}',f'Available artifacts for sale: {len(self.artifacts)}\n***']

        sorted_purchases: list[BaseCollector] = sorted(self.collectors,key = lambda c: (-len(c.purchased_artifacts),c.name))
        for collector in sorted_purchases:
            result.append(collector.__str__())

        return '\n'.join(result)