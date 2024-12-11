from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def match_jobs_to_candidate(candidate_skills, job_skills):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([candidate_skills, job_skills])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    return similarity[0][0]

def calculate_candidate_score(info, job):
    score = 0

    # Vérifiez que les compétences du candidat et du job sont définies
    if info.skills and job.skills_required:
        # Transformez les compétences en ensembles pour faciliter la comparaison
        candidate_skills = set(info.skills.lower().split(', '))
        job_skills = set(job.skills_required.lower().split(', '))

        # Calculer l'intersection entre les compétences du job et celles du candidat
        matching_skills = candidate_skills.intersection(job_skills)

        # Attribuez des points pour chaque compétence correspondante
        score += len(matching_skills) * 10  # Par exemple, 10 points par compétence correspondante

    # Vérifiez la localisation (bonus si les localisations correspondent)
    if info.location and job.location and info.location.lower() == job.location.lower():
        score += 5  # Bonus pour la localisation correspondante

    return score




from django.shortcuts import get_object_or_404
from .models import Job
from info.models import Info

def get_ranked_candidates(job_id):
    job = get_object_or_404(Job, pk=job_id)
    candidates = Info.objects.all()

    scored_candidates = []
    for candidate in candidates:
        score = calculate_candidate_score(candidate, job)
        scored_candidates.append({
            'candidate': candidate,
            'score': score
        })

    return sorted(scored_candidates, key=lambda x: x['score'], reverse=True)

