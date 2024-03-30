import numpy as np
from sklearn.metrics import diversity_score

class DiverseAIWorkforce:
    """
    A class to promote diversity, equity, and inclusion in the AI workforce.
    """
    
    def __init__(self, protected_attributes):
        """
        Initialize the DiverseAIWorkforce with the specified protected attributes.
        
        Args:
            protected_attributes (list): A list of protected attributes to consider in the workforce diversity initiatives.
        """
        self.protected_attributes = protected_attributes
    
    def analyze_workforce_demographics(self, workforce_data):
        """
        Analyze the demographics of the AI workforce.
        
        Args:
            workforce_data (dict): A dictionary containing workforce demographic data, with keys representing different attributes.
        
        Returns:
            dict: A dictionary containing the analysis results, including representation percentages for each protected attribute.
        """
        analysis_results = {}
        
        for attr in self.protected_attributes:
            attr_data = workforce_data[attr]
            attr_categories, attr_counts = np.unique(attr_data, return_counts=True)
            attr_percentages = attr_counts / len(attr_data) * 100
            
            analysis_results[attr] = {
                'categories': attr_categories.tolist(),
                'percentages': attr_percentages.tolist()
            }
        
        return analysis_results
    
    def identify_underrepresented_groups(self, analysis_results, threshold=20):
        """
        Identify underrepresented groups in the AI workforce based on the analysis results.
        
        Args:
            analysis_results (dict): A dictionary containing the workforce demographic analysis results.
            threshold (float): The threshold percentage below which a group is considered underrepresented.
        
        Returns:
            dict: A dictionary containing the underrepresented groups for each protected attribute.
        """
        underrepresented_groups = {}
        
        for attr, results in analysis_results.items():
            underrepresented = [cat for cat, pct in zip(results['categories'], results['percentages']) if pct < threshold]
            underrepresented_groups[attr] = underrepresented
        
        return underrepresented_groups
    
    def develop_diversity_initiatives(self, underrepresented_groups):
        """
        Develop targeted initiatives to increase diversity and inclusion in the AI workforce.
        
        Args:
            underrepresented_groups (dict): A dictionary containing the underrepresented groups for each protected attribute.
        
        Returns:
            dict: A dictionary containing the proposed diversity initiatives for each underrepresented group.
        """
        diversity_initiatives = {}
        
        for attr, groups in underrepresented_groups.items():
            initiatives = []
            
            for group in groups:
                if attr == 'gender':
                    initiatives.append(f"Launch targeted recruitment campaign for {group} in AI roles")
                    initiatives.append(f"Establish mentorship program for {group} in AI career development")
                elif attr == 'race/ethnicity':
                    initiatives.append(f"Partner with {group} professional organizations for AI talent sourcing")
                    initiatives.append(f"Provide scholarships for {group} students in AI-related fields")
                elif attr == 'age':
                    initiatives.append(f"Develop returnship program for {group} professionals transitioning to AI careers")
                    initiatives.append(f"Offer upskilling opportunities for {group} employees in AI technologies")
            
            diversity_initiatives[attr] = initiatives
        
        return diversity_initiatives
    
    def implement_inclusive_hiring_practices(self, job_descriptions, resume_screening_criteria):
        """
        Implement inclusive hiring practices to mitigate bias in AI workforce recruitment.
        
        Args:
            job_descriptions (list): A list of job descriptions for AI roles.
            resume_screening_criteria (dict): A dictionary containing the criteria for resume screening.
        
        Returns:
            tuple: A tuple containing the updated job descriptions and resume screening criteria.
        """
        updated_job_descriptions = []
        
        for job_description in job_descriptions:
            # Remove gender-coded language from job descriptions
            job_description = job_description.replace("aggressive", "assertive").replace("competitive", "collaborative")
            
            # Emphasize commitment to diversity and inclusion
            job_description += "\nWe are an equal opportunity employer and value diversity at our company."
            
            updated_job_descriptions.append(job_description)
        
        updated_screening_criteria = resume_screening_criteria.copy()
        
        # Remove potentially biased criteria from resume screening
        updated_screening_criteria.pop("university_ranking", None)
        updated_screening_criteria.pop("years_of_experience", None)
        
        # Add inclusive criteria to resume screening
        updated_screening_criteria["diversity_contributions"] = "Contributions to diversity and inclusion in previous roles or extracurricular activities"
        
        return updated_job_descriptions, updated_screening_criteria
    
    def evaluate_diversity_progress(self, workforce_data, baseline_data):
        """
        Evaluate progress towards diversity and inclusion goals in the AI workforce.
        
        Args:
            workforce_data (dict): A dictionary containing the current workforce demographic data.
            baseline_data (dict): A dictionary containing the baseline workforce demographic data.
        
        Returns:
            dict: A dictionary containing the diversity progress metrics for each protected attribute.
        """
        progress_metrics = {}
        
        for attr in self.protected_attributes:
            current_data = workforce_data[attr]
            baseline_data = baseline_data[attr]
            
            current_diversity = diversity_score(current_data)
            baseline_diversity = diversity_score(baseline_data)
            
            progress_metrics[attr] = {
                'current_diversity': current_diversity,
                'baseline_diversity': baseline_diversity,
                'change': current_diversity - baseline_diversity
            }
        
        return progress_metrics