from project.artifacts.base_artifact import BaseArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.base_collector import BaseCollector
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    VALID_ARTIFACTS:list[BaseArtifact] =  [RenaissanceArtifact,ContemporaryArtifact]
    VALID_COLLECTORS: list[BaseCollector] = [Museum,PrivateCollector]

    def __init__(self):
        self.artifacts: list[BaseArtifact] = []
        self.collectors: list[BaseCollector] = []
        self.__artifacts_sold = 0

    def register_artifact(self,artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int)->str:
        artifact_class:type[BaseArtifact]|None = next((a for a in self.VALID_ARTIFACTS
                                                       if a.__name__ == artifact_type),None)

        if artifact_class is None:
            raise ValueError("Unknown artifact type!")

        if any(a.name == artifact_name for a in self.artifacts):
            raise ValueError(f"{artifact_name} has been already registered!")


        artifact = artifact_class(artifact_name,artifact_price,artifact_space)
        self.artifacts.append(artifact)

        return f"{artifact_name} is successfully added to the auction as {artifact_type}."


    def register_collector(self,collector_type: str, collector_name: str) ->str:
        collector_class :type[BaseCollector] | None = next((c for c in self.VALID_COLLECTORS
                                                          if c.__name__ == collector_type),None)

        if collector_class is None:
            raise ValueError("Unknown collector type!")

        if any(c.name == collector_name for c in self.collectors):
            raise ValueError(f"{collector_name} is successfully registered as a {collector_type}.")

        collector = collector_class(collector_name)
        self.collectors.append(collector)

        return f"{collector_name} is successfully registered as a {collector_type}."


    def perform_purchase(self,collector_name: str, artifact_name: str):
        collector = next((c for c in self.collectors if c.name == collector_name),None)
        artifact = next((a for a in self.artifacts if a.name == artifact_name),None)

        if collector is None:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")

        if artifact is None:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")

        if not collector.can_purchase(artifact.price,artifact.space_required):
            return "Purchase is impossible."

        self.artifacts.remove(artifact)
        self.__artifacts_sold += 1
        collector.purchased_artifacts.append(artifact)
        collector.available_money -= artifact.price
        collector.available_space -= artifact.space_required

        return f"{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}."

    def remove_artifact(self,artifact_name: str):
        artifact = next((a for a in self.artifacts if a.name == artifact_name),None)

        if artifact is None:
            return  "No such artifact."

        self.artifacts.remove(artifact)
        return f"Removed {artifact.artifact_information()}"

    def fundraising_campaigns(self,max_money: float):
        collectors:list[BaseCollector] = [c for c in self.collectors if c.available_money < max_money]
        [c.increase_money() for c in collectors]

        return f"{len(collectors)} collector/s increased their available money."

    def get_auction_report(self):

        result = ["**Auction statistics**",
                  f"Total number of sold artifacts: {self.__artifacts_sold}",
                  f"Available artifacts for sale: {len(self.artifacts)}",
                  "***"]

        collectors_sorted = sorted(self.collectors,key = lambda c: (-len(c.purchased_artifacts),c.name))
        [result.append(str(c)) for c in collectors_sorted]

        return '\n'.join(result)
