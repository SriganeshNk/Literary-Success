__author__ = 'santhosh'

from util import NovelMetaGenerator
from util import ml_util
from feature_wise_predictor import POSFeatureUtil

def testPOSFeatures(genres=None):
    core_nlp_files_dict = NovelMetaGenerator.listGenreWiseFileNames(NovelMetaGenerator.CORE_NLP_BASE,\
                                                                    NovelMetaGenerator.CORE_NLP_TAG_FILES_PATTERN)
    meta_dict = NovelMetaGenerator.loadInfoFromMetaFile()
    if not genres:
        genres = NovelMetaGenerator.ALL_GENRES

    for genre in genres:
        core_nlp_files = core_nlp_files_dict[genre]
        meta_dict_for_genre = meta_dict[genre]
        feature_dict = POSFeatureUtil.extractPOSFeaturesFromCoreNLPFiles(core_nlp_files)
        train_data, train_result, test_data, test_result =\
            ml_util.splitTrainAndTestData(meta_dict_for_genre, feature_dict, split=0.8)
        scores = ml_util.doClassfication(train_data, train_result, test_data, test_result)
        print scores


testPOSFeatures(genres=set(['Adventure Stories']))

