from circleguard import ReplayPath, ReplayMap, Map, KeylessCircleguard, Mod

from tests.utils import CGTestCase, RES


class TestReplays(CGTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.kcg = KeylessCircleguard()

    def test_loading_replaypath(self):
        r = ReplayPath(RES / "example_replay.osr")
        self.kcg.load(r)
        self.assertRaises(ValueError, lambda: r.map_id)
        self.assertRaises(ValueError, lambda: r.user_id)
        self.assertEqual(r.mods, Mod.HD + Mod.DT, "Mods was not correct")
        self.assertEqual(r.replay_id, 2029801532, "Replay id was not correct")
        self.assertEqual(r.username, "MarthXT", "Username was not correct")
        self.assertTrue(r.loaded, "Loaded status was not correct")

    def test_loading_other_loadables(self):
        r = ReplayMap(221777, 2757689)
        m = Map(221777, "1")
        self.assertRaises(NotImplementedError, lambda: self.kcg.load(r))
        self.assertRaises(NotImplementedError, lambda: self.kcg.load(m))
        self.assertRaises(NotImplementedError, lambda: self.kcg.load_info(m))
