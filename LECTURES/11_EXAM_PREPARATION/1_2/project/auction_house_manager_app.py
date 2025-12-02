from operator import attrgetter

from pandas.io.sas.sas_constants import column_type_length

from project.artifacts.base_artifact import BaseArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.base_collector import BaseCollector
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    sold_artefacts = 0
    def __init__(self):
        self.artifacts: list[BaseArtifact] = []
        self.collectors: list[BaseCollector] = []

    def register_artifact(self,artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        artifact_types = {"RenaissanceArtifact":RenaissanceArtifact,
                           "ContemporaryArtifact":ContemporaryArtifact}

        if artifact_type not in artifact_types.keys():
            raise ValueError("Unknown artifact type!")

        artifact = next((a for a in self.artifacts if a.name == artifact_name),None)

        if artifact:
            raise ValueError(f"{artifact_name} has been already registered!" )

        artifact = artifact_types[artifact_type](artifact_name,artifact_price,artifact_space)
        self.artifacts.append(artifact)

        return  f"{artifact_name} is successfully added to the auction as {artifact_type}."


    def register_collector(self,collector_type: str, collector_name: str):
        collector_types = {"Museum": Museum,
                          "PrivateCollector": PrivateCollector}

        if collector_types not in collector_type:
            raise  ValueError("Unknown collector type!")

        collector = next((c for c in self.collectors if c.name == collector_name),None)

        if collector:
            raise ValueError(f"{collector_name} has been already registered!")

        collector =  collector_types[collector_type](collector_name)
        self.collectors.append(collector)
        return f"{collector_name} is successfully registered as a {collector_type}."



    def perform_purchase(self,collector_name: str, artifact_name: str):
        collector = next((c for c in self.collectors if c.name == collector_name),None)
        artifact = next((a for a in self.artifacts if a.name == artifact_name),None)

        if not collector:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")

        if not artifact:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")

        can_buy = collector.can_purchase(artifact.price,artifact.space_required)

        if not can_buy:
            return "Purchase is impossible."

        #actions after purchase
        self.sold_artefacts += 1
        self.artifacts.remove(artifact) #remove from auction
        collector.purchased_artifacts.append(artifact)
        collector.available_money -= artifact.price
        collector.available_space -= artifact.space_required

        return f"{collector_name} purchased {artifact_name} for a price of {artifact.price}."

    def remove_artifact(self, artifact_name: str):
        artifact = next((a for a in self.artifacts if a.name == artifact_name),None)

        if not artifact:
            return "No such artifact."

        self.artifacts.remove(artifact)
        return f"Removed  {artifact.artifact_information()}"

    def fundraising_campaigns(self,max_money: float):
        count = 0

        for collector in self.collectors:
            if collector.available_money <= max_money:
                collector.increase_money()
                count += 1

        return  f"{count} collector/s increased their available money."


    def get_auction_report(self):
        result = f"**Auction statistics**\nTotal number of sold artifacts: {self.sold_artefacts}\nAvailable artifacts for sale: {len(self.artifacts)}\n***\n"

        sorted_collectors = sorted(self.collectors, key = lambda x: x.purchaes)
