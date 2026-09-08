class Solution:
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        hours = 0

        # Energy needed
        total_energy = sum(energy) + 1

        if initialEnergy < total_energy:
            hours += total_energy - initialEnergy

        # Experience needed
        current_experience = initialExperience

        for i in range(len(experience)):
            if current_experience <= experience[i]:
                needed = experience[i] + 1 - current_experience
                hours += needed
                current_experience += needed

            current_experience += experience[i]

        return hours
